"""
This script is used to plot the results of the doubling experiment test by changing the num_test and
the algorithm in exam.
"""

import pandas as pd
import matplotlib.pyplot as plt


# function to determine which column is varying and which is constant
def determine_columns(df):
    # Controlla se il numero di nodi è costante
    if df['num_nodes'].nunique() == 1:
        constant_value = df['num_nodes'].iloc[0]
        varying_col = 'num_edges'
        varying_label = 'Number of Edges'
        constant_label = f'Number of Nodes = {constant_value}'
    # Altrimenti, controlla se il numero di archi è costante
    elif df['num_edges'].nunique() == 1:
        constant_value = df['num_edges'].iloc[0]
        varying_col = 'num_nodes'
        varying_label = 'Number of Nodes'
        constant_label = f'Number of Edges = {constant_value}'
    else:
        raise ValueError("Both 'num_nodes' and 'num_edges' vary. One must be constant per file.")

    return varying_col, varying_label, constant_label


# function to plot the csv file
def plot_from_csv(csv_file, title):
    # load the csv file into a pandas dataframe
    df = pd.read_csv(csv_file)

    # determines which column is varying and which is constant
    varying_col, varying_label, constant_label = determine_columns(df)

    # data extract
    x_data = df['execution_time']
    y_data = df[varying_col]

    # plot
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, marker='o', linestyle='-', color='b')

    # labels
    plt.xlabel('Execution Time (seconds)')
    plt.ylabel(varying_label)
    plt.title(f'{title} - {constant_label}')

    # show grid and plot
    plt.grid(True)
    plt.show()


if __name__ == '__main__':

    """ RESULTS PLOTTER """

    # list of available tests for Stoer-Wagner and NetworkX edge connectivity
    num_test_list = ['test_1_1', 'test_1_2', 'test_1_3', 'test_1_4', 'test_1_5', 'test_1_6',
                     'test_2_1', 'test_2_2', 'test_2_3', 'test_2_4', 'test_2_5', 'test_2_6']

    # choose between the available tests in num_test_list to display
    num_test = num_test_list[2]

    # list of available algorithms
    algorithm_list = ['stoer_wagner', 'ford_fulkerson', 'networkx_edge_connectivity']

    # choose between the available algorithms in algorithm_list to display
    algorithm = algorithm_list[0]

    # csv file to plot
    csv_file = algorithm + '/results/generated_graphs/' + algorithm + '_' + 'results' + '_' + num_test + '.csv'

    # graph title
    title = 'Performance Analysis'

    # plot
    plot_from_csv(csv_file, title)
