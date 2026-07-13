# Weekly-Challenge-25-Dijkstra-s-Algorithm
New schedule, new algorithms! I am now officially kicking off my coding challenges every Monday to start the week with maximum focus. For Week 25, I tackled one of the most important optimization algorithms in modern software engineering: **Dijkstra's Algorithm**.


##  Description
New schedule, new algorithms! I am now officially kicking off my coding challenges every Monday to start the week with maximum focus. For Week 25, I tackled one of the most important optimization algorithms in modern software engineering: **Dijkstra's Algorithm**.

While BFS (which I coded in Week 23) is great for unweighted grids, Dijkstra is built for the real world. It finds the absolute shortest path between nodes in a graph where edges have different "weights" (representing traffic, distance, or financial cost). It is the mathematical foundation behind GPS navigation systems and internet packet routing.

## How it works
Dijkstra uses a **Greedy Approach** paired with a **Priority Queue (Min-Heap)**. 
1. It maintains a record of the minimum distance from the start node to every other node, initially set to infinity.
2. The Priority Queue ensures the algorithm always explores the node with the lowest accumulated cost next.
3. **Edge Relaxation:** As it explores neighbors, if it discovers a route that is cheaper than the currently recorded distance, it updates the record and pushes the new path into the queue.
4. It repeats this until the target destination is reached with the mathematically proven lowest cost.

##  Complexity Analysis
* **Time Complexity:** $O(V + E \log V)$ - Where $V$ is the number of vertices and $E$ is the number of edges. The $\log V$ factor comes from extracting the minimum value from the Priority Queue (Heap).
* **Space Complexity:** $O(V)$ - To store the distances dictionary, the previous nodes dictionary, and the priority queue.

## Dependencies
* Python 3.12 (Standard Library: `heapq`)
* Matplotlib.pyplot
* NetworkX
