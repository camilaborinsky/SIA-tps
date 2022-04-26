from turtle import color
from matplotlib import pyplot as plt
import numpy as np

def method_vs_error(gd_errors, cg_errors, adam_errors):
    plt.figure(1)
    #vector of three colors in red hue
    colors = plt.cm.Reds(np.linspace(0.5,1,3))
    #bar graph of avarage error vs method with standard deviation
    plt.bar(["Gradiente descendente", "Gradiente conjugado", "Método Adam"], [np.mean(gd_errors), np.mean(cg_errors), np.mean(adam_errors)], yerr=[np.std(gd_errors), np.std(cg_errors), np.std(adam_errors)], color=colors)
    
    plt.xlabel("Método")
    plt.ylabel("Error")
    


def method_vs_time(gd_times, cg_times, adam_times):
    plt.figure(2)
    #vector of three colors in red hue
    colors = plt.cm.Reds(np.linspace(0.5,1,3))
    #bar graph of avarage time vs method with standard deviation
    plt.bar(["Gradiente descendente", "Gradiente conjugado", "Método Adam"], [np.mean(gd_times), np.mean(cg_times), np.mean(adam_times)], yerr=[np.std(gd_times), np.std(cg_times), np.std(adam_times)], color=colors)
    plt.xlabel("Método")
    plt.ylabel("Tiempo")
    plt.show()



