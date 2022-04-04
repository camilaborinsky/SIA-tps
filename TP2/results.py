



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
