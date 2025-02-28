from collections import defaultdict
import numpy as np
from scipy.sparse import csr_matrix
import sys

def read_graph(file_path):
    """
    Reads a graph from a file and returns a dictionary representing the adjacency list.
    Each node and its outgoing links are parsed.
    """
    graph = defaultdict(list)
    max_node = -1  # Start with -1 to ensure even an empty file results in a correct n of 0.
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            node = int(parts[0])
            max_node = max(max_node, node)  # Update max_node with the highest node number seen so far.
            if len(parts) > 1 and parts[1]:
                linked_nodes = list(map(int, parts[1].split(',')))
                max_node = max(max_node, *linked_nodes)  # Also check linked nodes to ensure all are counted.
            else:
                linked_nodes = []
            graph[node] = linked_nodes
    return graph, max_node + 1  # max_node + 1 because node indices start at 0

def create_sparse_matrix(graph, n):
    """
    Converts a graph dictionary to a sparse matrix representation.
    Here, rows are target nodes and columns are source nodes.
    """
    row_indices = []
    col_indices = []
    data = []

    for source_node, target_nodes in graph.items():
        if target_nodes:
            weight = 1 / len(target_nodes)
            for target_node in target_nodes:
                row_indices.append(target_node)
                col_indices.append(source_node)
                data.append(weight)
        else:
            # Here, no explicit handling required, as these nodes should contribute to the teleport probability uniformly.
            continue

    # Create the CSR matrix
    matrix = csr_matrix((data, (row_indices, col_indices)), shape=(n, n))
    return matrix


def pagerank(matrix, n, damping=0.85, tol=1e-6):
    """
    Computes the PageRank of each node using the power iteration method until convergence.

    Parameters:
        matrix (csr_matrix): The sparse matrix representation of the graph.
        n (int): Number of nodes.
        damping (float): Damping factor for PageRank.
        tol (float): Tolerance for convergence.
    """
    # Initialize the rank vector with equal probabilities
    rank = np.ones(n) / n
    # print(f"Initial rank distribution: {rank}")

    # Teleportation vector (handles dead ends)
    teleport = np.ones(n) / n * (1 - damping)
    # print(f"Teleportation vector: {teleport}")

    count = 0
    while True:
        count += 1
        new_rank = damping * matrix.dot(rank) + teleport
        # Check convergence
        if np.linalg.norm(new_rank - rank, 1) <= tol:
            # print(f"Converged after {count} iterations.")
            break
        rank = new_rank

    # print(f"Final PageRank distribution: {rank}")
    # print(f"Sum of the PageRank distribution: {rank.sum()}")

    return rank,count

def experiment(input_file,d_values=np.arange(0.75, 1.00, 0.05)):
    graph,nodes = read_graph(input_file)
    sparse_matrix = create_sparse_matrix(graph, nodes)
    for d in d_values:
        ranks, iterations = pagerank(sparse_matrix, nodes, damping=d)
        print(f"Damping Factor: {d}, Iterations Taken: {iterations}, Top PageRank: {np.max(ranks)}")



def main(input_file, damping_factor):
    graph,nodes = read_graph(input_file)
    sparse_matrix = create_sparse_matrix(graph,nodes)
    ranks,iterations = pagerank(sparse_matrix, nodes, damping=float(damping_factor))

    # Print the PageRank vector to stdout in scientific notation
    for rank in ranks:
        print(f"{round(rank,10)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python PageRank.py input.txt d ")
    else:
        input_file = sys.argv[1]
        damping_factor = sys.argv[2]
        main(input_file, damping_factor)
        # experiment(input_file)