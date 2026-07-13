import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Weekly Challange 25: Dijkstra's Algorithm
# Author: Ing. Arturo Javier Borbon Rojas

def dijkstra(graph, start, target):
    print(f"Starting... | Origin:{start} Destination:{target}")

    # Priority queue to store accumulated cost and urrent node
    pq=[(0,start)]

    # Dictionary to store the minimum cost to reach each node
    distances= {node: float("infinity") for node in graph}
    distances[start]=0

    # Dictionary to reconstruct the final optimal path
    previous_nodes= {node: None for node in graph}

    step = 1
    while pq:
        # The priority queue automatically pops the nod with the lowest accumulated cost
        current_distance, current_node= heapq.heappop(pq)

        # optimization if we reached the target, we can stop evaluating
        if current_node == target:
            print(f"Target {target} reached")
            break

        # If we pulled a stale, more expensive route from the queue, skip it
        if current_distance > distances[current_node]:
            continue

        print(f"Step {step} | Exploring Node {current_node} | Cost {current_distance}")

        # Check all neighboring connections
        for neighbor, weight in graph[current_node].items():
            distance=current_distance + weight

            if distance < distances[neighbor]:
                print(f"Cheaper route found to {neighbor}: {distance} | Prevously {distances[neighbor]}")
                distances[neighbor]= distance
                previous_nodes[neighbor]=current_node
                #push the new, better route into the priority queue
                heapq.heappush(pq, (distance, neighbor))

        step+=1

    print("-"*50)

  # Reconstruct path by walking backwards from target to start
    path=[]
    current= target
    while current is not None:
      path.insert(0, current)
      current= previous_nodes[current]

    if distances[target] == float("infinity"):
        print(f"No route exists to {target}")
    else:
        print(f"Optimal Route Found {" to ".join(path)}")
        print(f"Total Cost (Distance/Time): {distances[target]}")

    return path, distances[target]


def visualize_route(graph_data, optimal_path):
    print("Generating visual map")

    # 1 Initialize a Network X graph
    G=nx.Graph()

    # 2 Populate the graph with nodes, edges, and weights
    for node, neighbors in graph_data.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    # 3 Create a layout 
    # Using a spring layout spaces them out nicely based on their connections
    pos= nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10,6))

    # 4 Draw the base graph 
    nx.draw(G,pos, with_labels=True, node_color="lightgray", node_size=2000, font_size=14, font_weight="bold", edge_color="gray", width=2)

    # 5 Add the text labels for the weights distance/cost on the edges
    edge_labels= nx.get_edge_attributes(G,"weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color="red")

    # 6 Highlight the optimal path in green
    if optimal_path:
        path_edges= [(optimal_path[i], optimal_path[i+1]) for i in range(len(optimal_path)-1)]
        nx.draw_networkx_nodes(G,pos, nodelist=optimal_path, node_color="lime", node_size=2000)
        nx.draw_networkx_edges(G,pos, edgelist=path_edges, edge_color="green", width=5)

    plt.title(f"Dijkstra's Optimal Route: {' ➔ '.join(optimal_path)}", fontsize=16, fontweight='bold')
    plt.axis('off') # Hide the grid axes
    plt.tight_layout()
    plt.show()


# Testing
network={
    "A": {"B":4, "C":2},
    "B": {"A":4, "E":3},
    "C": {"A":2, "D":2, "F":4},
    "D": {"C":2, "E":3},
    "E": {"B":3, "D":3, "F":1},
    "F": {"C":4, "E":1}
}

dijkstra(network,"A", "E")


# 1. Calculate the ruote
ruta_ganadora, costo_total = dijkstra(network, 'A', 'E')

# 2. Visualize
if ruta_ganadora:
    visualize_route(network, ruta_ganadora)
