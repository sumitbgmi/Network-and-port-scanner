import socket
import threading
from queue import Queue
from datetime import datetime

# -----------------------------
# Common Ports
# -----------------------------
COMMON_PORTS = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-Proxy"
}

# -----------------------------
# Banner
# -----------------------------
print("=" * 50)
print("      Python Network & Port Scanner")
print("=" * 50)

target = input("Enter IP or Domain: ").strip()

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("\n[-] Invalid Host")
    exit()

print(f"\nTarget : {target}")
print(f"IP      : {target_ip}")

start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

print("\nScanning...\n")

queue = Queue()
lock = threading.Lock()
results = []

start_time = datetime.now()

# -----------------------------
# Scan Function
# -----------------------------
def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target_ip, port))

    if result == 0:
        service = COMMON_PORTS.get(port, "Unknown")

        banner = ""

        try:
            s.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = s.recv(1024).decode(errors="ignore").strip()
        except:
            banner = "No Banner"

        with lock:
            print(f"[OPEN] {port:<6} {service}")

            results.append(
                f"Port {port} OPEN | Service: {service}\nBanner: {banner}\n"
            )

    s.close()

# -----------------------------
# Worker Thread
# -----------------------------
def worker():
    while True:
        port = queue.get()

        scan(port)

        queue.task_done()

# -----------------------------
# Create Threads
# -----------------------------
for i in range(100):
    thread = threading.Thread(target=worker)
    thread.daemon = True
    thread.start()

# -----------------------------
# Add Ports
# -----------------------------
for port in range(start_port, end_port + 1):
    queue.put(port)

queue.join()

end_time = datetime.now()

print("\nFinished!")

print("Time Taken:", end_time - start_time)

# -----------------------------
# Save Report
# -----------------------------
filename = "scan_report.txt"

with open(filename, "w") as file:

    file.write(f"Target : {target}\n")
    file.write(f"IP : {target_ip}\n\n")

    for item in results:
        file.write(item)
        file.write("\n")

print(f"\nReport saved as {filename}")