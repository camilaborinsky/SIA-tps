import time
import graphs as g
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
    initial_errors = []
    gd_errors = []
    cg_errors = []
    adam_errors = []
    gd_times = []
    cg_times = []
    adam_times = []

    random.seed(1)

    for j in range(0,20):
        print("============START=============")
        values = []
        for n in range(11):
            values.append(random.uniform(-10,10))
        ind:Individual = Individual(values)
        initial_errors.append(error(ind.genotype, expected_output, reagents))

        #print(str(ind))
        init_time= time.time()
        res_gd = minimize_gd(ind, expected_output, reagents) #res.x me da el mejor individuo y res.fun el valor del error para el x
        end_time = time.time()
        print("Gradiente descendente")
        print(f"Tiempo de ejecución :{end_time-init_time}")
        print(f"Individuo: {res_gd.x}")
        print(f"Valor de error: {res_gd.fun}")
        dif_time_1 = end_time - init_time
        gd_times.append(dif_time_1)
        gd_errors.append(res_gd.fun)

        init_time= time.time()
        res_cg = minimize_cg(ind, expected_output, reagents) #res.x me da el mejor individuo y res.fun el valor del error para el x
        end_time = time.time()
        print("Gradiente conjugado")
        print(f"Tiempo de ejecución :{end_time-init_time}")
        print(f"Individuo: {res_cg.x}")
        print(f"Valor de error: {res_cg.fun}")
        dif_time_2 = end_time - init_time
        cg_times.append(dif_time_2)
        cg_errors.append(res_cg.fun)

        init_time= time.time()
        res_adam = minimize_adam(ind, expected_output, reagents, 10) #res.x me da el mejor individuo y res.fun el valor del error para el x
        end_time = time.time()
        print("Método Adam")
        print(f"Tiempo de ejecución :{end_time-init_time}")
        print(f"Individuo: {res_adam}")
        print(f"Valor de error: {error(res_adam, expected_output, reagents)}")
        dif_time_3 = end_time - init_time
        adam_times.append(dif_time_3)
        adam_errors.append(error(res_adam, expected_output, reagents))
        
        print("============END=============")
    #g.initial_error_vs_errors(initial_errors, gd_errors, cg_errors, adam_errors)
    g.method_vs_error(gd_errors, cg_errors, adam_errors)
    g.method_vs_time(gd_times, cg_times, adam_times)

main()