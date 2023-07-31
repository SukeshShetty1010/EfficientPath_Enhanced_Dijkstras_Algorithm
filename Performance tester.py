import timeit
from Normal_Dijkstras_Algorithm import dijkstra as normal_dijkstra
from Optimized_Dijkstras_Algorithm import dijkstra as optimized_dijkstra
from Optimized_Dijkstras_Algorithm import Graph

# Function to create the custom graph instance (the same graph for both algorithms)
def create_custom_graph():
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
    
    return custom_graph

# Function to measure the execution time of normal Dijkstra's algorithm
def measure_normal_dijkstra(graph):
    normal_dijkstra(graph, "A")

# Function to measure the execution time of optimized Dijkstra's algorithm
def measure_optimized_dijkstra(graph):
    optimized_dijkstra(graph, "A")

# Create the custom graph instance
custom_graph = create_custom_graph()

# Measure execution time of normal Dijkstra's algorithm
normal_time = timeit.timeit(lambda: measure_normal_dijkstra(custom_graph), number=1000)

# Measure execution time of optimized Dijkstra's algorithm
optimized_time = timeit.timeit(lambda: measure_optimized_dijkstra(custom_graph), number=1000)

# Calculate the speedup factor
speedup_factor = normal_time / optimized_time

# Print the results
print(f"Execution time of normal Dijkstra's algorithm: {normal_time:.6f} seconds")
print(f"Execution time of optimized Dijkstra's algorithm: {optimized_time:.6f} seconds")

if speedup_factor > 1:
    print(f"The optimized Dijkstra's algorithm is {speedup_factor:.2f} times faster than the normal version.")
elif speedup_factor < 1:
    print(f"The normal Dijkstra's algorithm is {1/speedup_factor:.2f} times faster than the optimized version.")
else:
    print("Both versions have similar execution times.")
