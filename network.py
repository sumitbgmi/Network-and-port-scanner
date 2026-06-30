import socket

def resolve_target(target):
    """
    Convert a domain name to an IP address.
    """

    try:
        ip = socket.gethostbyname(target)
        return ip

    except socket.gaierror:
        return None