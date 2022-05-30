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
    bplot = ax.boxplot(data, patch_artist=True)
    # array de tonos azules

    colors = ["#099c72", "#46b49d", "#3997a3", "#035887", "#7195db", "#3776ce", "#0460db", "#bdd3f3"]
    for patch, color in zip(bplot['boxes'],colors) :
        patch.set_facecolor(color)
    # make median color dark grey
    for median in bplot["medians"]:
        median.set_color("#333333")
    ax.set_xlabel(xlabel)
    aux = list(range(1, data.shape[1]+1))
    plt.xticks(aux, x_ticks)
    ax.set_title(title)
    if filename is not None:
        plt.savefig(filename)
    # ax.set_ylabel(ylabel)