import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def make_boxplot(data, title, xlabel, ylabel, x_ticks, filename):
    """
    Generate a boxplot for the given data.
    """

    sns.set_style("whitegrid")
    sns.set_context("paper")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.boxplot(data)
    ax.set_xlabel(xlabel)
    aux = list(range(1, data.shape[1]+1))
    plt.xticks(aux, x_ticks)
    ax.set_title(title)
    if filename is not None:
        plt.savefig(filename)
    # ax.set_ylabel(ylabel)