import socket

# Port tarama fonksiyonu
def scan_ports(target_ip, start_port=1, end_port=65535):
    print(f"Scanning {target_ip} for open ports...")

    open_ports = [] # Açık portların listesi

    # Portları tarama
    for port in range(start_port, end_port+1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket oluştur
            sock.settimeout(1) # Zaman aşımı ayarı
            resoult = socket.connect_ex((target_ip, port)) # Port'a bağlanmayı dene

            if resoult == 0:
                open_ports.append(port) # Açık portları listeye ekle
                print(f"Port {port} is open")
            sock.close() # Socket'i kapat
        except Exception:
            pass
    
    if len(open_ports) == 0: # Eğer açık port yoksa
        print("No open ports found")

    return open_ports
