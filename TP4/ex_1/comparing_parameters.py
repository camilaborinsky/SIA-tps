from networks.kohonen import KohonenNetwork
from utils.file_utils import parse_countries_data, standarize_data
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

def update_radius_constant(initial_radius, k, epoch_limit):
    return initial_radius

def update_radius_linear(initial_radius, k, epoch_limit):
    return (1-initial_radius)*k/(28*epoch_limit) + initial_radius

def update_radius_exp(initial_radius, k, epoch_limit):
    return (initial_radius-1)*np.exp(-5*k/(28*epoch_limit)) + 1

def update_learn_rate_constant(initial_learning_rate, k, epoch_limit):
    return initial_learning_rate

def update_learn_rate_linear(initial_learning_rate, k, epoch_limit):
    return -initial_learning_rate*k/(epoch_limit*28) + initial_learning_rate

def update_learn_rate_exp(initial_learning_rate, k, epoch_limit):
    return initial_learning_rate*np.exp(-5*k/(28*(epoch_limit)))


execution_count = 10


def main():
    output_dim_values = range(2, 7)

    update_radius_fns = [update_radius_constant, update_radius_linear, update_radius_exp]
    update_learning_rate_fns = [update_learn_rate_constant, update_learn_rate_linear, update_learn_rate_exp]

    attributes, countries, dataset = parse_countries_data("ex_1/resources/europe.csv")
    std = standarize_data(dataset)

    #nro de epocas
    epoch_limit = 500*7

    # dimension de input
    input_dim = len(attributes)

    # tasa de aprendizaje inicial
    initial_learning_rate = 1

    # función de actualización de tasa de aprendizaje
    update_learning_rate = update_learn_rate_exp

    #función de actualización de radio
    update_radius = update_radius_exp
    q_errors = [None]*execution_count
    for output_dimension in output_dim_values:
        # radio inicial
        initial_radius = np.ceil(output_dimension*output_dimension/2)

        for j in range(execution_count):
            q_errors[j] = []
            kohonen = KohonenNetwork(input_dim, output_dimension, initial_learning_rate, initial_radius, update_radius, update_learning_rate, random_weights=False)
            kohonen.train(std, countries, epoch_limit, callback=None)
            q_error = kohonen.get_quantization_error(std)
            q_errors[j].append(q_error)
            print(f"output_dimension: {output_dimension}, execution: {j}, q_error: {q_error}")
    
    plt.plot(output_dim_values, np.mean(q_errors, axis=0))
    
main()

            


