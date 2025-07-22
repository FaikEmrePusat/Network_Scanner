from scapy.all import IP, ICMP, sr

# ICMP ping işlemi
def icmp_ping(ip_list):
    # IP listesindeki her IP adresi için ping işlemi yap
    for ip in ip_list:
        pkt = IP(dst=ip) / ICMP() # ICMP paketi oluştur
        ans, _ = sr(pkt, timeout=5, verbose=False) # Ping işlemi yap
        if ans:
            print(f"ICMP ping başarılı: {ip}")
        else:
            print(f"ICMP ping başarısız: {ip}")