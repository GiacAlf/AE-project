"""
This script is used to execute the doubling experiment with Stoer-Wagner algorithm on
the generated simple undirected graphs created by validation_graphs_creator.py, or simply the ones
that are uploaded, stored in local tests_graphs/generated_graphs.
The script runs all the algorithms and saves their results in local results/generated_graphs in a CSV file only
if the check about simple graphs is true.
"""

import os
from tests.graph_test_execution import check_all_graphs, run_stoer_wagner_on_graphs, run_ford_fulkerson_on_graphs, \
    run_networkx_edge_connectivity_on_graphs


# function to run the algorithm
def run_algorithm(algorithm, input_dir, output_file):
    if algorithm in algorithm_functions:
        algorithm_functions[algorithm](input_dir, output_file)
    else:
        print(f"Algorithm {algorithm} not recognized.")


""" test_1_1: fixed number of nodes = 64, doubled number of edges """
""" test_1_2: fixed number of nodes = 128, doubled number of edges """
""" test_1_3: fixed number of nodes = 256, doubled number of edges """
""" test_1_4: fixed number of nodes = 512, doubled number of edges """
""" test_1_5: fixed number of nodes = 1024, doubled number of edges """
""" test_1_6: fixed number of nodes = 2048, doubled number of edges """

""" test_2_1: fixed number of edges = 1024, doubled number of nodes """
""" test_2_2: fixed number of edges = 1500, doubled number of nodes """
""" test_2_3: fixed number of edges = 2000, doubled number of nodes """
""" test_2_4: fixed number of edges = 4096, doubled number of nodes """
""" test_2_5: fixed number of edges = 6000, doubled number of nodes """
""" test_2_6: fixed number of edges = 8000, doubled number of nodes """

if __name__ == '__main__':

    # list of available tests
    num_test_list = ['test_1_1', 'test_1_2', 'test_1_3', 'test_1_4', 'test_1_5', 'test_1_6',
                     'test_2_1', 'test_2_2', 'test_2_3', 'test_2_4', 'test_2_5', 'test_2_6']

    # list of available algorithms
    algorithm_list = ['stoer_wagner', 'ford_fulkerson', 'networkx_edge_connectivity']

    # map of algorithms to their functions
    algorithm_functions = {
        'stoer_wagner': run_stoer_wagner_on_graphs,
        'ford_fulkerson': run_ford_fulkerson_on_graphs,
        'networkx_edge_connectivity': run_networkx_edge_connectivity_on_graphs
    }

    # choose between the available algorithms in algorithm_list to display
    algorithm = algorithm_list[0]

    output_dir = algorithm + '/results/generated_graphs'

    # creates the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for i in range(len(num_test_list)):
        try:
            print(f"Starting the doubling experiment test with {algorithm} algorithm...")

            # input directory
            input_dir = 'test_graphs/generated_graphs' + '_' + num_test_list[i]

            # checks if all the graphs in the input directory are simple, undirected, not empty and not isolated
            if check_all_graphs(input_dir):
                print(f"\nAll input test graphs are simple and undirected, not empty and not isolated. "
                      f"Running {algorithm} algorithm...")

                output_file = ('results/generated_graphs/' + algorithm + '_results' + '_' +
                               num_test_list[i] + '.csv')

                run_algorithm(algorithm, input_dir, output_file)

            else:
                print("Not all input test graphs are simple and undirected. Execution aborted.")

        except Exception as e:
            print(f"Error: {e}")
