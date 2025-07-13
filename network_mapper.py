import netifaces

def get_gatwey_ip():
    gw = netifaces.gateways()
    print(gw['default'][netifaces.AF_INET][0])

get_gatwey_ip()