"""
This script is used to generate a fixed number of simple graphs using
test/graphs_creation.generate_and_save_graphs function with a fixed number of nodes and a fixed
number of edges, saving them in CSV files in local tests_graphs/generated_graphs.
"""

from tests.graphs_creation import generate_and_save_graphs


if __name__ == '__main__':

    """ STOER-WAGNER AND NETWORKX DOUBLING EXPERIMENTS GRAPHS CREATION """
    """ In this main nodes or edges are fixed to generate graphs """
    """
    # TEST 1: doubling number of edges keeping number of nodes constant

    # test 1.1: fixed number of nodes = 64, doubled number of edges
    nodes_list = [64, 64, 64, 64, 64]
    edges_list = [64, 128, 256, 512, 1024]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_1_1'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 1.2: fixed number of nodes = 128, doubled number of edges
    nodes_list = [128, 128, 128, 128, 128, 128]
    edges_list = [128, 256, 512, 1024, 2048, 4096]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_1_2'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 1.3: fixed number of nodes = 256, doubled number of edges
    nodes_list = [256, 256, 256, 256, 256, 256, 256]
    edges_list = [256, 512, 1024, 2048, 4096, 8192, 16384]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_1_3'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 1.4: fixed number of nodes = 512, doubled number of edges
    nodes_list = [512, 512, 512, 512, 512, 512, 512, 512]
    edges_list = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_1_4'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 1.5: fixed number of nodes = 1024, doubled number of edges
    nodes_list = [1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024]
    edges_list = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_1_5'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 1.6: fixed number of nodes = 2048, doubled number of edges
    nodes_list = [2048, 2048, 2048, 2048, 2048, 2048, 2048, 2048, 2048, 2048]
    edges_list = [2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_1_6'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # TEST 2: doubling number of nodes keeping number of edges constant.

    # test 2.1: fixed number of edges = 1024, doubled number of nodes
    nodes_list = [64, 128, 256, 512, 1024]
    edges_list = [1024, 1024, 1024, 1024, 1024]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_2_1'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 2.2: fixed number of edges = 1500, doubled number of nodes
    nodes_list = [64, 128, 256, 512, 1024]
    edges_list = [1500, 1500, 1500, 1500, 1500]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_2_2'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 2.3: fixed number of edges = 2000, doubled number of nodes
    nodes_list = [64, 128, 256, 512, 1024]
    edges_list = [2000, 2000, 2000, 2000, 2000]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_2_3'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 2.4: fixed number of edges = 4096, doubled number of nodes
    nodes_list = [128, 256, 512, 1024, 2048, 4096]
    edges_list = [4096, 4096, 4096, 4096, 4096, 4096]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_2_4'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 2.5: fixed number of edges = 6000, doubled number of nodes
    nodes_list = [128, 256, 512, 1024, 2048, 4096]
    edges_list = [6000, 6000, 6000, 6000, 6000, 6000]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_2_5'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 2.6: fixed number of edges = 8000, doubled number of nodes
    nodes_list = [128, 256, 512, 1024, 2048, 4096]
    edges_list = [8000, 8000, 8000, 8000, 8000, 8000]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_2_6'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)
    """

    """ FORF-FULKERSON DOUBLING EXPERIMENTS GRAPHS CREATION """
    # TEST 1: doubling number of edges keeping number of nodes constant

    # test 1.1: fixed number of nodes = 6, doubled number of edges
    nodes_list = [6, 6, 6]
    edges_list = [5, 10, 15]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs_ff/generated_graphs_test_1_1'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 1.2: fixed number of nodes = 12, doubled number of edges
    nodes_list = [12, 12, 12]
    edges_list = [15, 30, 45]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs_ff/generated_graphs_test_1_2'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 1.3: fixed number of nodes = 24, doubled number of edges
    nodes_list = [24, 24, 24, 24]
    edges_list = [25, 50, 100, 200]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs_ff/generated_graphs_test_1_3'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 1.4: fixed number of nodes = 48, doubled number of edges
    nodes_list = [48, 48, 48, 48, 48]
    edges_list = [50, 100, 200, 400, 800]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs_ff/generated_graphs_test_1_4'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 1.5: fixed number of nodes = 96, doubled number of edges
    nodes_list = [96, 96, 96, 96, 96]
    edges_list = [100, 200, 400, 800, 1600]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs_ff/generated_graphs_test_1_5'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 1.6: fixed number of nodes = 128, doubled number of edges
    nodes_list = [128, 128, 128, 128, 128]
    edges_list = [200, 400, 800, 1600, 3200]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs_ff/generated_graphs_test_1_6'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # TEST 2: doubling number of nodes keeping number of edges constant.

    # test 2.1: fixed number of edges = 50, doubled number of nodes
    nodes_list = [12, 24, 48]
    edges_list = [50, 50, 50]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs_ff/generated_graphs_test_2_1'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 2.2: fixed number of edges = 100, doubled number of nodes
    nodes_list = [24, 48, 96]
    edges_list = [100, 100, 100]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs_ff/generated_graphs_test_2_2'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 2.3: fixed number of edges = 150, doubled number of nodes
    nodes_list = [24, 48, 96]
    edges_list = [150, 150, 150]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs_ff/generated_graphs_test_2_3'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 2.4: fixed number of edges = 200, doubled number of nodes
    nodes_list = [24, 48, 96, 192]
    edges_list = [200, 200, 200, 200]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs_ff/generated_graphs_test_2_4'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 2.5: fixed number of edges = 250, doubled number of nodes
    nodes_list = [24, 48, 96, 192]
    edges_list = [250, 250, 250, 250]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs_ff/generated_graphs_test_2_5'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 2.6: fixed number of edges = 400, doubled number of nodes
    nodes_list = [48, 96, 192, 384]
    edges_list = [400, 400, 400, 400]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs_ff/generated_graphs_test_2_6'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)
