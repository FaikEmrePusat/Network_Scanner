from scapy.all import IP, ICMP, sr

# ICMP ping işlemi
def icmp_ping(ip_list):
    for ip in ip_list:
        pkt = IP(dst=ip) / ICMP()
        ans, _ = sr(pkt, timeout=5, verbose=False)
        if ans:
            print(f"ICMP ping başarılı: {ip}")
        else:
            print(f"ICMP ping başarısız: {ip}")