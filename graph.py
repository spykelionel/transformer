import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
nodes = ["C1", "C2", "C3", "C4", "C5", "C6", "DGA", "SFRA", "PD Measurement", "Visual Inspection",
         "Gas tight syringe Argon purges vials", "Gas chromatography headspace sampling", "Calculator",
         "Tester", "Smart sweep algorithm", "SFRAv6.2"]
G.add_nodes_from(nodes)

# Add edges
edges = [
    ("C1", "DGA"), ("C2", "DGA"), ("C3", "DGA"),
    ("C2", "Gas chromatography headspace sampling"),
    ("C3", "Calculator"),
    ("C4", "Tester"),
    ("C5", "Smart sweep algorithm"),
    ("C6", "SFRA"),
    ("C6", "PD Measurement"),
    ("DGA", "Gas tight syringe Argon purges vials"),
    ("Gas chromatography headspace sampling", "Gas tight syringe Argon purges vials"),
    ("Tester", "SFRAv6.2")
]
G.add_edges_from(edges)

# Add labels to nodes
labels = {node: node for node in nodes}

# Visualize the graph
pos = nx.spring_layout(G, seed=42)  # Set the layout for better visualization
nx.draw(G, pos, with_labels=True, labels=labels, font_weight='bold', node_size=1000, node_color='lightblue', font_size=8, edge_color='gray', width=0.5)
plt.title("Transformer Diagnostic Methods Graph")
plt.show()
