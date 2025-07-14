import networkx as nx
import matplotlib.pyplot as plt
from network_mapper import get_gateway_ip
from inventory_scanner import scan_inventory

def create_graph(devices, router_ip):
    G = nx.Graph()
    G.add_node(router_ip)

    for device in devices:
        device_ip = device["ip"]
        G.add_node(device_ip)
        G.add_edge(router_ip, device_ip)

    # Son olarak grafiği çiz
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, font_size=10)
    plt.title("Network Topology Map")
    plt.show()