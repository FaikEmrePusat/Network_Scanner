from asyncio import futures
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket oluştur
        sock.settimeout(1) # Zaman aşımı ayarı
        result = socket.connect_ex((target_ip, port)) # Port'a bağlanmayı dene
        sock.close() # Socket'i kapat
        if result == 0:
            return port
    except Exception:
        pass
    return None

def scan_ports(target_ip, start_port=1, end_port=65535, max_workers=100):
    print(f"Scanning {target_ip} for open ports...")

    open_ports = [] # Açık portların listesi

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        
        futures = [executor.submit(check_port, target_ip, port) for port in range(start_port, end_port+1)]

        for future in as_completed(futures):
            port = future.result()
            if port is not None:
                open_ports.append(port)
                print(f"Port {port} is open.")
    if not open_ports:
        print("No open ports found.")
    return open_ports
        

"""# Port tarama fonksiyonu


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

    return open_ports"""