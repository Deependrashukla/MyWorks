import heapq

def dijkstra(graph, source):
    distances = {}
    for node in graph:
        distances[node] = float('infinity')
    distances[source] = 0
    priority_queue = [(0, source)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(priority_queue, (distance, adjacent))
    
    return distances

#graph
graph = {
    'S': {'A': 2, 'B': 1},
    'A': {'B': -2},
    'B': {}
}
# 9045902339, 224123, RAZA@123, 93598624Aa@, yaallah786, 8869020aA@l
source_node = 'S'
shortest_distances = dijkstra(graph, source_node)
print("Shortest distances from source node", source_node, ":", shortest_distances)
source_node = 'A'
shortest_distances = dijkstra(graph, source_node)
print("Shortest distances from source node", source_node, ":", shortest_distances)
source_node = 'B'
shortest_distances = dijkstra(graph, source_node)
print("Shortest distances from source node", source_node, ":", shortest_distances)
