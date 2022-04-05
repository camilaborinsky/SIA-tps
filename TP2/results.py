



from cProfile import label
import csv
import random
from turtle import color
from matplotlib import pyplot as plt
import numpy as np

from utils.file_utils import get_file_base

cross_labels = ["uniform", "multiple", "simple"]
mutation_labels = ["uniform", "normal"]
selection_labels = ["elite", "roulette", "rank", "tournament", "boltzmann", "truncated"]
breaks_labels = ["generation_count", "time", "acceptable_solution", "constant_solution"]
colors =["green", "blue", "red", "yellow", "orange", "purple"]
parent_selection_labels = ["random", "sorted", "balanced"]



def compare_cross(parent_selection, selection):
    mutation = 'uniform'
    out_file = f"output/cmp/cmp_cross_{selection}_generation_count_{mutation}_{parent_selection}"
    gen_axis = range(100)
    plt.figure(1)
    plt.title("Promedio de fitness por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Promedio de fitness")
    plt.figure(2)
    plt.title("Diversidad genética por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Diversidad genética")
    plt.figure(3)
    plt.title("Diversidad de fitness por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Diversidad de fitness")
 

    for cr, idx in cross_labels:
        fn = f"output/average/0_{get_file_base(selection, 'generation_count', cr, mutation, parent_selection)}_avg.csv"
        f = open(fn)
        r = list(csv.reader(f))
        for i in range(len(r[0])):
            data = [r[x][i] for x in range(len(r))]
            plt.figure(i+1)
            plt.plot(gen_axis, data, color=colors[idx], label=f"{cr}")

    plt.figure(1)
    plt.savefig(f"{out_file}_avg.png")
    plt.figure(2)
    plt.savefig(f"{out_file}_gen-div.png")
    plt.figure(3)
    plt.savefig(f"{out_file}_fit-div.png")
    plt.show()

def compare_selection(parent_selection, cross):
    mutation = 'uniform'
    out_file = f"output/cmp/cmp_selection_generation_count_{cross}_{mutation}_{parent_selection}"
    gen_axis = range(100)
    # figure, axis = plt.subplots(2, 3)
    plt.figure(1)
    plt.title("Promedio de fitness por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Promedio de fitness")
    plt.figure(2)
    plt.title("Diversidad genética por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Diversidad genética")
    plt.figure(3)
    plt.title("Diversidad de fitness por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Diversidad de fitness")
 

    for sel, idx in selection_labels:
        fn = f"output/average/0_{get_file_base(sel, 'generation_count', cross, mutation, parent_selection)}_avg.csv"
        f = open(fn)
        r = list(csv.reader(f))
        for i in range(len(r[0])):
            data = [r[x][i] for x in range(len(r))]
            plt.figure(i+1)
            plt.plot(gen_axis, data, color=colors[idx], label=f"{sel}")

    plt.figure(1)
    plt.savefig(f"{out_file}_avg.png")
    plt.figure(2)
    plt.savefig(f"{out_file}_gen-div.png")
    plt.figure(3)
    plt.savefig(f"{out_file}_fit-div.png")
    plt.show()

def compare_mutation(selection, parent_selection, cross):
    out_file = f"output/cmp/cmp_mutation_{selection}_generation_count_{cross}_{parent_selection}"
    gen_axis = range(100)
    # figure, axis = plt.subplots(2, 3)
    plt.figure(1)
    plt.title("Promedio de fitness por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Promedio de fitness")
    plt.figure(2)
    plt.title("Diversidad genética por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Diversidad genética")
    plt.figure(3)
    plt.title("Diversidad de fitness por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Diversidad de fitness")
 

    for mut, idx in mutation_labels:
        fn = f"output/average/0_{get_file_base(selection, 'generation_count', cross, mut, parent_selection)}_avg.csv"
        f = open(fn)
        r = list(csv.reader(f))
        for i in range(len(r[0])):
            data = [r[x][i] for x in range(len(r))]
            plt.figure(i+1)
            plt.plot(gen_axis, data, color=colors[idx], label=f"{mut}")

    plt.figure(1)
    plt.savefig(f"{out_file}_avg.png")
    plt.figure(2)
    plt.savefig(f"{out_file}_gen-div.png")
    plt.figure(3)
    plt.savefig(f"{out_file}_fit-div.png")
    plt.show()

def compare_parent_selection(selection, cross):
    mutation = 'uniform'
    out_file = f"output/cmp/cmp_parent_selection_{selection}_generation_count_{cross}_{mutation}"
    gen_axis = range(100)
    # figure, axis = plt.subplots(2, 3)
    plt.figure(1)
    plt.title("Promedio de fitness por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Promedio de fitness")
    plt.figure(2)
    plt.title("Diversidad genética por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Diversidad genética")
    plt.figure(3)
    plt.title("Diversidad de fitness por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Diversidad de fitness")
 

    for sel, idx in parent_selection_labels:
        fn = f"output/average/0_{get_file_base(selection, 'generation_count', cross, 'uniform', sel)}_avg.csv"
        f = open(fn)
        r = list(csv.reader(f))
        for i in range(len(r[0])):
            data = [r[x][i] for x in range(len(r))]
            plt.figure(i+1)
            plt.plot(gen_axis, data, color=colors[idx], label=f"{sel}")

    plt.figure(1)
    plt.savefig(f"{out_file}_avg.png")
    plt.figure(2)
    plt.savefig(f"{out_file}_gen-div.png")
    plt.figure(3)
    plt.savefig(f"{out_file}_fit-div.png")
    plt.show()

def compare_breaks(selection, cross, parent_selection):
    mutation = 'uniform'
    out_file = f"output/cmp/cmp_breaks_{selection}_{cross}_{mutation}_{parent_selection}"
    gen_axis = range(100)
    # figure, axis = plt.subplots(2, 3)
    plt.figure(1)
    plt.title("Promedio de fitness por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Promedio de fitness")
    plt.figure(2)
    plt.title("Diversidad genética por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Diversidad genética")
    plt.figure(3)
    plt.title("Diversidad de fitness por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Diversidad de fitness")
 

    for sel, idx in parent_selection_labels:
        fn = f"output/average/0_{get_file_base(selection, 'generation_count', cross, 'uniform', sel)}_avg.csv"
        f = open(fn)
        r = list(csv.reader(f))
        for i in range(len(r[0])):
            data = [r[x][i] for x in range(len(r))]
            plt.figure(i+1)
            plt.plot(gen_axis, data, color=colors[idx], label=f"{sel}")

    plt.figure(1)
    plt.savefig(f"{out_file}_avg.png")
    plt.figure(2)
    plt.savefig(f"{out_file}_gen-div.png")
    plt.figure(3)
    plt.savefig(f"{out_file}_fit-div.png")
    plt.show()

def generate_graph(filename, exec_variants):
    files = [open(f"output/average/{x}_{filename}_avg.csv") for x in range(exec_variants)]
    readers = [list(csv.reader(x, delimiter=",")) for x in files]
    labels = ["mean", "max", "min", "gen-div", "fit-div"]
    data = np.zeros((len(readers[0][0]), len(readers), len(readers[0])))
    # data_rows = [0]* len(readers[0])
    # data_files = [data_rows]*len(readers)
    # data_metrics = [data_files]*len(readers[0][0])
    # data = data_metrics
    for i in range(len(readers)):
        for x in range(len(readers[0])):
            for j in range(len(readers[0][0])):
                data[j,i,x] = round(float(readers[i][x][j]), 3)

    gen_axis = range(len(readers[0]))
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
    # figure, axis = plt.subplots(2, 3)
    plt.figure(1)
    plt.title("Promedio de fitness por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Promedio de fitness")
    for i in range(len(data[0])):
        plt.plot(gen_axis, data[0][i], color=colors[i])
    plt.savefig(f"output/graphs/ind/{filename}_{labels[0]}.png")

    plt.figure(2)
    plt.title("Máximo fitness por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Máximo fitness")
    for i in range(len(data[1])):
        plt.plot(gen_axis, data[1][i], color=colors[i])
    plt.savefig(f"output/graphs/ind/{filename}_{labels[1]}.png")

    
    plt.figure(3)
    plt.title("Mínimo fitness por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Mínimo fitness")
    for i in range(len(data[2])):
        plt.plot(gen_axis, data[2][i], color=colors[i])
    plt.savefig(f"output/graphs/ind/{filename}_{labels[2]}.png")


    plt.figure(4)
    plt.title("Diversidad genética por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Diversidad genética")
    for i in range(len(data[3])):
        plt.plot(gen_axis, data[3][i], color=colors[i])
    plt.savefig(f"output/graphs/ind/{filename}_{labels[3]}.png")
    

    plt.figure(5)
    plt.title("Diversidad de fitness por generación")
    plt.xlabel("Número de generación")
    plt.ylabel("Diversidad de fitness")
    for i in range(len(data[4])):
        plt.plot(gen_axis, data[4][i], color=colors[i])
    plt.savefig(f"output/graphs/ind/{filename}_{labels[4]}.png")

   
    plt.show()

def parent_selection_random_sample():
    return random.sample(["random", "balanced", "sorted"])

def selection_random_sample():
    return ["roulette, boltzmann"].append(random.sample(["elite", "truncated"]))

def cross_sample():
    return ["uniform", "multiple"]

def generate_comparison_files():
    for parent_sel in parent_selection_random_sample():
        for sel in selection_random_sample():
            compare_cross(parent_sel, sel)
            for cr in cross_sample():
                compare_mutation(sel, parent_sel, cr)
                compare_breaks(sel, cr, parent_sel)
    
    for cr in cross_sample():
        for sel in selection_random_sample():
            compare_parent_selection(sel, cr)
        for parent_sel in parent_selection_random_sample():
            compare_selection(parent_sel, cr)    


# generate_comparison_files()
# generate_graph("elite_generation_count_multiple_uniform", 5)