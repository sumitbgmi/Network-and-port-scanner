from network import resolve_target
from scanner import scan_port

print("=" * 50)
print("Python Network & Port Scanner")
print("=" * 50)

target = input("Enter IP or Domain: ")

ip = resolve_target(target)

if not ip:
    print("Invalid Host")
    exit()

print(f"\nTarget : {target}")
print(f"IP      : {ip}")

start_port = int(input("\nStart Port : "))
end_port = int(input("End Port   : "))

print("\nScanning...\n")

for port in range(start_port, end_port + 1):

    is_open, service = scan_port(ip, port)

    if is_open:
        print(f"[OPEN] Port {port:<5} Service: {service}")

print("\nScan Complete!")