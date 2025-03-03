class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        # Step 1: Initialize distances from src to all other vertices as infinite
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: Check for negative-weight cycles
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # No negative-weight cycles found, print shortest distances
        print("Vertex Distance from Source:")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")


# Example usage:
g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, -2)
g.add_edge(1, 3, 3)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

g.bellman_ford(1)


import networkx as nx
import matplotlib.pyplot as plt

# Example graph:
edges = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, -2),
    (1, 3, 3),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

# Create a directed graph object
G = nx.DiGraph()

# Add edges to the graph
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Create positions for nodes
pos = nx.spring_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=10)

plt.title('Example Graph')
plt.show()
