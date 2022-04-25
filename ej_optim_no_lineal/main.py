import time
from numpy import random
from functions import error

from individual import Individual
from optimization_methods import minimize_adam, minimize_cg, minimize_gd


def main():
    reagents = [
    [4.4793, -4.0765, -4.0765],
    [-4.1793, -4.9218, 1.7664],
    [-3.9429, -0.7689, 4.883]
    ]
    expected_output =  [0, 1, 1]
    values =[]
    print("============START=============")
    for n in range(11):
        values.append(random.uniform(-10,10))

    ind:Individual = Individual(values)
    print(str(ind))
    init_time= time.time()
    res = minimize_gd(ind, expected_output, reagents) #res.x me da el mejor individuo y res.fun el valor del error para el x
    end_time = time.time()
    print("Gradiente descendente")
    print(f"Tiempo de ejecución :{end_time-init_time}")
    print(f"Individuo: {res.x}")
    print(f"Valor de error: {res.fun}")
    init_time= time.time()
    res = minimize_cg(ind, expected_output, reagents) #res.x me da el mejor individuo y res.fun el valor del error para el x
    end_time = time.time()
    print("Gradiente conjugado")
    print(f"Tiempo de ejecución :{end_time-init_time}")
    print(f"Individuo: {res.x}")
    print(f"Valor de error: {res.fun}")
    init_time= time.time()
    res = minimize_adam(ind, expected_output, reagents) #res.x me da el mejor individuo y res.fun el valor del error para el x
    end_time = time.time()
    print("Gradiente conjugado")
    print(f"Tiempo de ejecución :{end_time-init_time}")
    print(f"Individuo: {res}")
    print(f"Valor de error: {error(res, expected_output, reagents)}")
    print("============END=============")


main()