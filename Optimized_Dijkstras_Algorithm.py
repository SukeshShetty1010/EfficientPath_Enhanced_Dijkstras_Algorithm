import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromnode, tonode, distance):
        self.edges[fromnode].append(tonode)
        self.distances[(fromnode, tonode)] = distance

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {initial: []}
    priority_queue = [(0, initial)]

    while priority_queue:
        current_weight, min_node = heapq.heappop(priority_queue)

        if min_node in visited and current_weight > visited[min_node]:
            continue

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = [min_node]
                heapq.heappush(priority_queue, (weight, edge))
            elif weight == visited[edge]:
                path[edge].append(min_node)

    return visited, path

# Create a custom graph instance
custom_graph = Graph()

# Add nodes to the graph
custom_graph.addNode("A")
custom_graph.addNode("B")
custom_graph.addNode("C")
custom_graph.addNode("D")
custom_graph.addNode("E")
custom_graph.addNode("F")
custom_graph.addNode("G")

# Add edges to the graph
custom_graph.addEdge("A", "B", 2)
custom_graph.addEdge("A", "C", 5)
custom_graph.addEdge("B", "C", 6)
custom_graph.addEdge("B", "D", 1)
custom_graph.addEdge("B", "E", 3)
custom_graph.addEdge("C", "F", 8)
custom_graph.addEdge("D", "E", 4)
custom_graph.addEdge("E", "G", 9)
custom_graph.addEdge("F", "G", 7)

def print_path_recursive(node, path):
    if node == "A":
        return ["A"]
    else:
        prev_node = path[node][0]
        prev_path = print_path_recursive(prev_node, path)
        return prev_path + [node]

# Perform Dijkstra's algorithm on the graph starting from node "A"
shortest_distances, shortest_paths = dijkstra(custom_graph, "A")

# Display the results
print("Shortest distances from node 'A':")
for node, distance in shortest_distances.items():
    print(f"From 'A' to '{node}': {distance}")

print("\nShortest paths from node 'A':")
for node, paths in shortest_paths.items():
    print(f"To '{node}':")
    if paths:
        for path in paths:
            path_str = " -> ".join(print_path_recursive(node, shortest_paths))
            print(path_str)
    else:
        print("No path found")