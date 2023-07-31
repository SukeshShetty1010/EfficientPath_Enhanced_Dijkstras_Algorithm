**Dijkstra's Algorithm Performance Comparison**

## Table of Contents
1. [Introduction](#introduction)
2. [Functionality](#functionality)
3. [Normal Dijkstra's Algorithm](#normal-dijkstras-algorithm)
4. [Optimized Dijkstra's Algorithm](#optimized-dijkstras-algorithm)
5. [DSA and OOPS Properties](#dsa-and-oops-properties)
6. [Time and Space Complexity](#time-and-space-complexity)
7. [Conclusion](#conclusion)

## Introduction <a name="introduction"></a>
This repository contains two implementations of Dijkstra's algorithm: a normal version and an optimized version. The purpose of this project is to compare the performance of these two implementations and demonstrate how the optimized version provides significant improvements in terms of time and space complexity.

## Functionality <a name="functionality"></a>
Dijkstra's algorithm is a popular algorithm used to find the shortest paths from a given source node to all other nodes in a weighted graph. The algorithm works by iteratively exploring the graph, updating the shortest distance to each node, and maintaining the shortest paths for each node. The normal and optimized versions of the algorithm both achieve the same functionality but with varying levels of efficiency.

## Normal Dijkstra's Algorithm <a name="normal-dijkstras-algorithm"></a>
The normal version of Dijkstra's algorithm is implemented using a simple priority queue to process nodes in ascending order of their distances. It explores all nodes in the graph while updating the distances and paths. However, this implementation has some inefficiencies, especially for large graphs, as it involves redundant operations and has higher time and space complexity.

## Optimized Dijkstra's Algorithm <a name="optimized-dijkstras-algorithm"></a>
The optimized version of Dijkstra's algorithm utilizes a more efficient priority queue implementation based on a binary heap, which significantly reduces the time complexity. This ensures that the algorithm explores the nodes in the most optimal order, resulting in faster execution times. Additionally, the optimized version reduces redundant operations, leading to improved space complexity.

## DSA and OOPS Properties <a name="dsa-and-oops-properties"></a>
Both implementations of Dijkstra's algorithm demonstrate the use of several data structures, such as defaultdict, set, and priority queue, to efficiently manage the graph and track visited nodes, distances, and paths. The object-oriented programming approach is utilized to encapsulate the graph-related functionality within the `Graph` class, promoting modularity and code reusability.

## Time and Space Complexity <a name="time-and-space-complexity"></a>
The time complexity of the normal Dijkstra's algorithm is O(V^2), where V is the number of nodes in the graph. In contrast, the optimized version achieves a time complexity of O((V + E) * log V), where E is the number of edges. This significant improvement in time complexity makes the optimized version much faster, especially for dense graphs.

Regarding space complexity, both versions use space proportional to the number of nodes and edges in the graph, leading to O(V + E) space complexity. However, due to the optimized version's more efficient priority queue implementation, it requires less overhead in practice, resulting in reduced memory usage.

## Conclusion <a name="conclusion"></a>
In conclusion, the optimized Dijkstra's algorithm is a major improvement over the normal version in terms of time and space complexity. The optimized version leverages a more efficient priority queue, which results in significantly faster execution times for large graphs. It achieves the same functionality as the normal version while requiring less memory and computational resources.

Please feel free to explore the code and the performance tester script to see the comparison results for yourself. If you have any questions or suggestions, please don't hesitate to reach out. Happy coding!
