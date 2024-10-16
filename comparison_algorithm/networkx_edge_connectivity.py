"""
This script is used to calculate the edge connectivity of a given graph using the built-in function in NetworkX
that has a time complexity of O(m+n*log(n))
"""

import networkx as nx
from graphs_utility_functions.graph_loader import GraphLoader


if __name__ == '__main__':

    """ FOR TESTING PURPOSES """

    try:
        # input directory for generated graphs
        file_path = '../graphs_utility_functions/generated_graphs/generated_graph_with_weights.csv'
        loader = GraphLoader(file_path)

        # load the graph from the CSV file with weights equal to 1
        graph = loader.load_graph_from_csv_with_weight()

        # Assert that the graph is not empty
        assert graph.number_of_nodes() > 0, "The graph must have at least one node"

        # Check for isolated nodes
        assert all(graph.degree(node) > 0 for node in graph.nodes()), "The graph contains isolated nodes"

        # print the number of nodes and edges
        print(f"Graph loaded with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")

        # Calculate edge connectivity using networkx
        edge_connectivity = nx.edge_connectivity(graph)

        # print the edge connectivity
        print(f"NetworkX edge connectivity value is: {edge_connectivity}")

    except Exception as e:
        print(f"Error: {e}")