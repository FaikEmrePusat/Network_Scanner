import socket

def scan_ports(target_ip, start_port=1, end_port=65535):
    print(f"Scanning {target_ip} for open ports...")

    open_ports = []

    for port in range(start_port, end_port+1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            resoult = socket.connect_ex((target_ip, port))

            if resoult == 0:
                open_ports.append(port)
                print(f"Port {port} is open")
            sock.close()
        except Exception:
            pass
    
    if len(open_ports) == 0:
        print("No open ports found")
    return open_ports
