import requests

def get_mac_vendor(mac):
    try:
        response = requests.get(f"https://api.macvendors.com/{mac}")
        if response.status_code == 200:
            return response.text.strip()

        else:
            return "Unknown"
    except:
        return "Unknown"