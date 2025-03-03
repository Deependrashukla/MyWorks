def bellman_ford(vertices, edges, src):
    dist = [float("Inf")] * vertices
    dist[src] = 0

    for _ in range(vertices - 1):
        for u, v, w in edges:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return

    print("Vertex Distance from Source:")
    for i in range(vertices):
        print(f"{i}\t\t\t{dist[i]}")

# New example graph represented as edge list
edges = [
    (0, 1, 1), (0, 2, 4),
    (1, 2, 3), (1, 3, 2), (1, 4, 2),
    (3, 2, 1), (3, 1, 1),
    (4, 3, -3)
]

# edges = [
#     (0, 1, 1), (1,2,1),(2,3,1),(3,4,-5),(4,2,1),(2,5,1)8
# ]

num_vertices =  5 # Number of vertices

# Source vertex
source_vertex = 0

# Run Bellman-Ford algorithm
bellman_ford(num_vertices, edges, source_vertex)