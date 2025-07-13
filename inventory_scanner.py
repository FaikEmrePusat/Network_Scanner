import scapy

import socket
import ipaddress


# ARP isteği gönderip cevap alan fonksiyon
def scan_inventory(subnet, include_vendor=True): # include_vendor: True ise vendor bilgisi döndürür, False ise döndürmez
    from scapy.all import ARP, Ether, srp
    from vendor_lookup import get_mac_vendor
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=subnet) # Ether: Ethernet paketi, ARP: ARP paketi
    answered, _ = srp(pkt, timeout=2, verbose=False) # srp: Send and Receive Packet
    
    devices = [] # cihazların bilgilerini tutacak liste

    for _, rcv in answered: # _: answered'ın ilk elemanı, rcv: answered'ın ikinci elemanı
        ip = rcv.psrc # rcv'in psrc alanı (IP adresi)
        mac = rcv.hwsrc # rcv'in hwsrc alanı (MAC adresi)
        vendor = get_mac_vendor(mac) if include_vendor else "Unknown" # get_mac_vendor: MAC adresinin üretici bilgisini döndürür

        devices.append({ # cihazların bilgilerini listeye ekle
            "ip": ip, # ip adresi
            "mac": mac, # mac adresi
            "vendor": vendor # üretici bilgisi
        })
    
    return devices # cihazların bilgilerini döndür


"""# ARP isteği gönderip cevap alan fonksiyon
def scan_inventory(subnet):
    # Broadcast paketle tüm cihazlara ARP isteği gönder
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=subnet) # Ether: Ethernet paketi, ARP: ARP paketi
    answered, _ = srp(pkt, timeout=2, verbose=False) # srp: Send and Receive Packet
    
    devices = []
    for _, rcv in answered: # _: answered'ın ilk elemanı, rcv: answered'ın ikinci elemanı
        devices.append({
            "ip": rcv.psrc,
            "mac": rcv.hwsrc
            "vendor": vendor
        })
    
    
    return devices"""

