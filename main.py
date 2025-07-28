import socket
import ipaddress
from inventory_scanner import scan_inventory
from network_mapper import get_gateway_ip
from create_graph import create_graph
from security_checks.icmp_ping import icmp_ping
from security_checks.port_scanner import scan_ports

# Ağ aralığını belirleme
def get_subnet():
    ip_range_choose = input("1'e basarsan: Ip aralığını kendin belirler.\n2'ye basarsan: Program otomatik olarak Ip aralığını belirler.")

    if ip_range_choose == "1": # Eğer 1 ise kullanıcıdan ip aralığını al
        subnet = input("Tarama yapılacak IP aralığını giriniz (192.168.1.0/24): ")

    elif ip_range_choose == "2": # Eğer 2 ise local ip adresini al
        local_ip = socket.gethostbyname(socket.gethostname())
        net = ipaddress.IPv4Network(local_ip + '/24', strict = False)
        subnet = str(net)


    else: # Eğer 1 veya 2 değilse programı sonlandır
        print("Geçerli bir değer giriniz")
        exit()  # Programı sonlandır
    return subnet

 # Ağ cihazlarının bilgilerini ekrana yazdır
def print_devices(devices):
    print("\nTarama Sonuçları:")
    for device in devices:
        print(f"IP: {device['ip']} | MAC: {device['mac']} | Vendor: {device['vendor']}")

 # Ana fonksiyon
if __name__ == "__main__":
    # Ağ tarama
    subnet = get_subnet()
    include_vendor = input("Vendor bilgisi alınsın mı? (e/h): ").lower() == "e"
    devices = scan_inventory(subnet, include_vendor)
    print_devices(devices)

    # Grafik oluşturma
    router_ip = get_gateway_ip()
    create_graph(devices, router_ip)
 
    # ICMP ping işlemi
    ip_list = [device["ip"] for device in devices]
    icmp_ping(ip_list)

    # Port tarama
    scan_ports(ip_list)