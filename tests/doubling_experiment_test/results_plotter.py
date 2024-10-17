"""
This script is used to plot the results of the doubling experiment test by changing the num_test and
the algorithm in exam.
It can be put in comparison with a fitting line, log, square or cubic function.
"""
import numpy as np
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
def plot_from_csv(csv_file, title, plot_line=False, plot_logarithmic=False,
                  plot_square=False, plot_cubic=False):
    # load the csv file into a pandas dataframe
    df = pd.read_csv(csv_file)

    # determines which column is varying and which is constant
    varying_col, varying_label, constant_label = determine_columns(df)

    # data extract
    x_data = df[varying_col]
    y_data = df['execution_time']

    # plot
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, marker='o', linestyle='-', color='grey', label='Algorithm')

    # Option to plot a line or a logarithmic curve
    if plot_line:
        # Fit a straight line using the least squares
        m, b = np.polyfit(x_data, y_data, 1)  # Line fitting

        plt.plot(x_data, m * x_data + b, color='red', linestyle='--', label='Best Line Fit')

    if plot_logarithmic:
        # Perform log(x) transformation and fit a line
        log_x_data = np.log(x_data)
        m_log, b_log = np.polyfit(log_x_data, y_data, 1)  # Linear regression on log-transformed x

        # Plot the fitted logarithmic curve (exp transformation)
        plt.plot(x_data, m_log * np.log(x_data) + b_log, color='green', linestyle='--',
                 label='Logarithmic Fit')

    if plot_square:
        # Plot quadratic fit (degree 2)
        p_quad = np.polyfit(x_data, y_data, 2)
        plt.plot(x_data, np.polyval(p_quad, x_data), color='blue', linestyle='--',
                 label='Quadratic Fit')

    if plot_cubic:
        # Plot cubic fit (degree 3)
        p_cubic = np.polyfit(x_data, y_data, 3)
        plt.plot(x_data, np.polyval(p_cubic, x_data), color='purple', linestyle='--',
                 label='Cubic Fit')

    # labels
    plt.ylabel('Execution Time (seconds)')
    plt.xlabel(varying_label)
    plt.title(f'{title} - {constant_label}')

    # show grid and plot
    plt.grid(True)
    plt.legend()  # Show legend to differentiate between the algorithm and other functions
    plt.show()


if __name__ == '__main__':

    """ RESULTS PLOTTER """

    # list of available algorithms
    algorithm_list = ['stoer_wagner', 'ford_fulkerson', 'networkx_edge_connectivity']

    """PARAMETER TO CHANGE: choose between the available algorithms in algorithm_list to display """
    algorithm = algorithm_list[1]

    # list of available tests for Stoer-Wagner and NetworkX edge connectivity
    num_test_list = ['test_1_1', 'test_1_2', 'test_1_3', 'test_1_4', 'test_1_5', 'test_1_6',
                     'test_2_1', 'test_2_2', 'test_2_3', 'test_2_4', 'test_2_5', 'test_2_6']

    # choose between the available tests in num_test_list to display
    num_test = num_test_list[9]

    # csv file to plot
    csv_file = (algorithm + '/results/generated_graphs/' + algorithm + '_' + 'results' +
                '_' + num_test + '.csv')

    # graph title
    title = 'Performance Analysis'

    # Choose the fit function to plot with True
    plot_from_csv(csv_file, title,
                  plot_line=False,
                  plot_logarithmic=False,
                  plot_square=True,
                  plot_cubic=False)
