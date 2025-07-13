import socket
import ipaddress
from inventory_scanner import scan_inventory

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


def print_devices(devices):
    print("\nTarama Sonuçları:")
    for device in devices:
        print(f"IP: {device['ip']} | MAC: {device['mac']} | Vendor: {device['vendor']}")


if __name__ == "__main__":
    subnet = get_subnet()
    include_vendor = input("Vendor bilgisi alınsın mı? (e/h): ").lower() == "e"
    devices = scan_inventory(subnet, include_vendor)
    print_devices(devices)