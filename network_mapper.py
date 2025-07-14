import netifaces

# Gateway IP adresini alan fonksiyon
def get_gateway_ip():
    gw = netifaces.gateways()
    return gw['default'][netifaces.AF_INET][0] # gw['default'][netifaces.AF_INET][0]: Gateway IP adresi