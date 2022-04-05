



import csv
from turtle import color
from matplotlib import pyplot as plt


def create_graph(generation, mean_fitness, max_fitness, min_fitness, gen_diveristy, fitness_diversity, gen_breach):
    figure, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(3, 3)

    ax1.set_xlabel('Número de generación')
    ax1.set_ylabel('Fitness promedio')
    ax1.scatter(generation, mean_fitness)

    ax2.set_xlabel('Número de generación')
    ax2.set_ylabel('Máximo fitness')
    ax2.scatter(generation, max_fitness)

    ax3.set_xlabel('Número de generación')
    ax3.set_ylabel('Mínimo fitness')
    ax3.scatter(generation, min_fitness)

    ax4.set_xlabel('Número de generación')
    ax4.set_ylabel('Diversidad de genes')
    ax1.scatter(generation, gen_diveristy)

    ax5.set_xlabel('Número de generación')
    ax5.set_ylabel('Diversidad de fitness')
    ax1.scatter(generation, fitness_diversity)

    ax6.set_xlabel('Número de generación')
    ax6.set_ylabel('Brecha generacional')
    ax1.scatter(generation, gen_breach)


    plt.savefig('/output/')
    plt.show()


def generate_graph(filename, exec_variants):
    files = [open(f"output/average/{x}_{filename}_avg.csv") for x in range(exec_variants)]
    readers = [list(csv.reader(x, delimiter=",")) for x in files]
    colors =["green", "blue", "red", "yellow", "orange", "purple"]
    data_rows = [0]* len(readers[0])
    data_files = [data_rows]*len(readers)
    data_metrics = [data_files]*len(readers[0][0])
    data = data_metrics
    for i in range(len(readers)):
        for x in range(len(readers[0])):
            for j in range(len(readers[0][0])):
                data[j][i][x] = round(float(readers[i][x][j]), 3)

    print(len(data))
    print(len(data[0]))
    print(len(data[0][0]))

    gen_axis = range(len(readers[0]))
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
    figure, axis = plt.subplots(2, 3)

    axis[0, 0].set_title("Promedio de fitness por generación")
    axis[0, 0].set_xlabel("Número de generación")
    axis[0, 0].set_ylabel("Promedio de fitness")

    axis[0, 1].set_title("Máximo fitness por generación")
    axis[0, 1].set_xlabel("Número de generación")
    axis[0, 1].set_ylabel("Máximo fitness")
    

    axis[0, 2].set_title("Mínimo fitness por generación")
    axis[0, 2].set_xlabel("Número de generación")
    axis[0, 2].set_ylabel("Mínimo fitness")

    axis[1, 0].set_title("Diversidad genética por generación")
    axis[1, 0].set_xlabel("Número de generación")
    axis[1, 0].set_ylabel("Diversidad genética")    

    axis[1, 1].set_title("Diversidad de fitness por generación")
    axis[1, 1].set_ylabel("Número de generación")
    axis[1, 1].set_title("Diversidad de fitness")
    for i in range(len(data[0])):
        axis[0, 0].plot(gen_axis, data[0][i], color=colors[i])
    for i in range(len(data[1])):
        axis[0, 1].plot(gen_axis, data[1][i], color=colors[i])
    for i in range(len(data[2])):
        axis[0, 2].plot(gen_axis, data[2][i], color=colors[i])
    for i in range(len(data[3])):
        axis[1, 0].plot(gen_axis, data[3][i], color=colors[i])
    for i in range(len(data[4])):
        axis[1, 1].plot(gen_axis, data[4][i], color=colors[i])



   
    plt.savefig("output/graphs/ind/{filename}.png")
    plt.show()
    

generate_graph("elite_generation_count_multiple_uniform", 5)