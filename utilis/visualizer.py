import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO

def create_graph(nodes, edges):
    """Create networkx graph from nodes and edges"""
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    for from_, to, amount in edges:
        G.add_edge(nodes[from_], nodes[to], weight=amount, label=str(amount))
    return G

def draw_graph(G, title):
    """Draw graph and return as image bytes"""
    pos = nx.spring_layout(G, k=1.5, iterations=200, seed=42)
    plt.figure(figsize=(14, 10))
    nx.draw(G, pos, with_labels=True, node_size=2500, node_color='skyblue',
            font_size=10, font_weight='bold', arrows=True, arrowsize=20)
    
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, 
                               font_color='red', font_size=9,
                               bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))
    
    plt.title(title, fontsize=14, pad=20)
    plt.tight_layout()
    
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf