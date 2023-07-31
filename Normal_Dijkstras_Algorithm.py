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
    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None or visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = [min_node]
            elif weight == visited[edge]:
                path[edge].append(min_node)

    return visited, path

# Usage example:
custom_graph = Graph()
custom_graph.addNode("A")
custom_graph.addNode("B")
custom_graph.addNode("C")
custom_graph.addNode("D")
custom_graph.addNode("E")

custom_graph.addEdge("A", "B", 4)
custom_graph.addEdge("A", "C", 2)
custom_graph.addEdge("B", "C", 5)
custom_graph.addEdge("B", "D", 10)
custom_graph.addEdge("C", "D", 3)
custom_graph.addEdge("D", "E", 7)

shortest_distances, shortest_paths = dijkstra(custom_graph, "A")

print("Shortest distances from node 'A':")
for node, distance in shortest_distances.items():
    print(f"From 'A' to '{node}': {distance}")

def print_path_recursive(node, path):
    if node == "A":
        return ["A"]
    else:
        prev_node = path[node][0]
        prev_path = print_path_recursive(prev_node, path)
        return prev_path + [node]

print("\nShortest paths from node 'A':")
for node, paths in shortest_paths.items():
    print(f"To '{node}':")
    if paths:
        for path in paths:
            path_str = " -> ".join(print_path_recursive(node, shortest_paths))
            print(path_str)
    else:
        print("No path found")