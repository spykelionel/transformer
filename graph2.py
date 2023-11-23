import networkx as nx
import matplotlib.pyplot as plt

# Your data
labels = ["C1", "C2", "C3", "C4", "C5", "C6"]
cost = [10, 20, 3, 70, 5, 300]
component_or_step_objectif = [
    "Take the oil samples and fill into Argon purges vials",
    "Vials equilibrated by sample loop in HSS and inject into GC",
    "Check if the ratios ranges satisfy the Roger’s High energy electrical discharge ratio range",
    "Connect the transformer to the analyzer and measure the different primary and secondary voltages and calculate the corresponding ratios",
    "Calculate the gains and plot the SFRA test for the different phases. (gain as a function of frequencies)",
    "Detect the presence of failure"
]
duration = [10, 5, 2, 5, 600, 15]

# Create a graph
G = nx.Graph()

# Add nodes with attributes
for i, label in enumerate(labels):
    G.add_node(label, cost=cost[i], objective=component_or_step_objectif[i], duration=duration[i])

# Add edges (assuming there is some relationship between components)
# You can modify this based on your specific use case
G.add_edges_from([("C1", "C2"), ("C2", "C3"), ("C3", "C4"), ("C4", "C5"), ("C5", "C6"), ("C6", "C1")])

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{G.nodes[u]["cost"]}, {G.nodes[u]["duration"]}' for u, v in G.edges})

plt.show()
