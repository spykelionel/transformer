import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
graph = nx.Graph()

# Add nodes to the graph
nodes = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']  # Extracted from the "Component (step)" column
graph.add_nodes_from(nodes)

# Add edges to represent relationships or dependencies
edges = [('C1', 'C2'), ('C2', 'C3'), ('C2', 'C4'), ('C2', 'C5'), ('C4', 'C6')]  # Example connections based on the table
graph.add_edges_from(edges)

# Add attributes or features to nodes and edges
attributes = {
    'C1': {
        'duration': 10,
        'personnel': 'Technician',
        'accuracy': 99,
        'type': 'Simple',
        'type_output': 'Sample oil',
        'origin': 'DGA'
    },
    'C2': {
        'duration': 20,
        'personnel': 'Technician',
        'accuracy': 97,
        'type': 'Simple',
        'type_output': 'Sample oil',
        'origin': 'DGA'
    },
    'C3': {
        'duration': 0,
        'personnel': 'Expert',
        'accuracy': 95,
        'type': 'Simple',
        'type_output': 'List of voltages (primary and secondary) and list of ratios',
        'origin': 'SFRA'
    },
    'C4': {
        'duration': 70,
        'personnel': 'Tester',
        'accuracy': None,
        'type': None,
        'type_output': None,
        'origin': 'the relocation of transformer. Earthquake, set of phase'
    },
    'C5': {
        'duration': 5,
        'personnel': 'Smart sweep algorithm',
        'accuracy': None,
        'type': None,
        'type_output': None,
        'origin': 'the relocation of transformer. Earthquake, set of phase'
    },
    'C6': {
        'duration': 30,
        'personnel': 'Expert',
        'accuracy': 95,
        'type': 'Simple',
        'type_output': 'Graph',
        'origin': 'SFRA'
    }
}

# Set node attributes
nx.set_node_attributes(graph, attributes)

# Print the graph information
# print("Nodes:", graph.nodes(data=True))
# print("Edges:", graph.edges())

# Generate the graphical representation
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(graph)  # Layout algorithm for node positioning
nx.draw(graph, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=10, font_weight='bold')

# Add node attributes as labels
labels = nx.get_node_attributes(graph, 'origin')
nx.draw_networkx_labels(graph, pos, labels=labels, font_color='black')

# Show the plot
plt.title("Graph Representation")
plt.axis('off')
plt.show()