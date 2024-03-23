import networkx as nx
import matplotlib.pyplot as plt

# Create a new graph
G = nx.Graph()

# Add nodes
people = [
    "Alice",
    "Bob",
    "Charlie",
    "Diana",
    "Fiona",
    "George",
    "Hannah",
    "Ian",
    "Judy",
]
G.add_nodes_from(people)

# Add edges with initial friendship relationships and weights
friendships = [
    ("Alice", "Bob"),
    ("Alice", "Charlie"),
    ("Alice", "Fiona"),
    ("Alice", "George"),
    ("Bob", "Diana"),
    ("Bob", "Hannah"),
    ("Charlie", "Ian"),
    ("Diana", "Judy"),
    ("Fiona", "George"),
    ("Fiona", "Hannah"),
    ("George", "Ian"),
    ("Hannah", "Judy"),
    ("Judy", "Alice"),
]

# Adding the relationships with their types and weights
for u, v, *w in friendships:
    G.add_edge(u, v, relationship="familiar", weight=4)

# Adding colleagues and family with specific relationships and weights
G.add_edge("Fiona", "Hannah", relationship="family", weight=1)
G.add_edge("Alice", "George", relationship="friendship", weight=2)
G.add_edge("Judy", "Alice", relationship="friendship", weight=2)
G.add_edge("Bob", "Hannah", relationship="friendship", weight=2)
G.add_edge("Bob", "Judy", relationship="colleagues", weight=3)
G.add_edge("Charlie", "Ian", relationship="colleagues", weight=3)

# Generate edge colors and widths based on relationship type and weight
edge_colors = []
for _, _, data in G.edges(data=True):
    if data["relationship"] == "familiar":
        edge_colors.append("red")
    elif data["relationship"] == "colleagues":
        edge_colors.append("orange")
    elif data["relationship"] == "friendship":
        edge_colors.append("yellow")
    elif data["relationship"] == "family":
        edge_colors.append("green")

weight_mapping = {4: 1, 3: 2, 2: 3, 1: 4}
edge_widths = [weight_mapping[data["weight"]] for _, _, data in G.edges(data=True)]


if __name__ == "__main__":
    # Display main characteristics
    print("Nodes count:", G.number_of_nodes())
    print("Edges count:", G.number_of_edges())
    print("Degree of nodes:", G.degree)

    # Position nodes using the spring layout
    pos = nx.spring_layout(G, seed=42)

    # Draw the network
    plt.figure(figsize=(12, 10))
    nx.draw_networkx(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        edge_color=edge_colors,
        width=edge_widths,
        node_size=2500,
        font_size=12,
        font_weight="bold",
    )

    plt.title("Social Network with Different Relationship Types")
    plt.show()
