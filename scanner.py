import socket
from services import COMMON_PORTS

def scan_port(ip, port):
    """
    Scan a single TCP port.
    Returns (True, service_name) if open,
    otherwise (False, None).
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((ip, port))

    sock.close()

    if result == 0:
        service = COMMON_PORTS.get(port, "Unknown")
        return True, service

    return False, None