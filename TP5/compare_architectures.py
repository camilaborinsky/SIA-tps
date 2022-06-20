from parser import data_converter, parse_config, sample_set

from matplotlib import pyplot as plt
from autoencoder import Autoencoder
import numpy as np

base_output_path = "output/sin_nada/"
def compare_architectures():
    
    #Parse config file
    config_json = parse_config("resources/config.json")

    training_set = list()
    testing_set = list()
    

    #Parse and sample training data
    for i in config_json["font_numbers"]:
        labels, alphabet = data_converter("resources/fonts_" + str(i) + ".txt")
        alphabet = np.array(alphabet)
        flattened_input = np.array(list(map(lambda char: np.array(char).flatten(), alphabet)))
        # if training_set is None:
        #     training_set = flattened_input
        # else:
        training_set.extend(sample_set(flattened_input, config_json["training_sample"]))
        testing_set.append(list(zip(labels, flattened_input)))
    latent_dimension = 2
    update_frequency = 0
    execution_count = 5
    input_dimension = len(training_set[0])
    activation_function = (lambda x: 1/(1+np.exp(-2*x)))
    activation_derivative = (lambda x: 2*(1/(1+np.exp(-2*x)))*(1-(1/(1+np.exp(-2*x)))) )
    update_learn_rate=bool(config_json["update_learn_rate"])


    for arch in config_json["architectures"]:
        for i in range(execution_count):
            ae = Autoencoder(input_dimension, arch, latent_dim=latent_dimension, 
            activation_function=activation_function,
            activation_function_derivative=activation_derivative, 
            update_learn_rate=update_learn_rate, 
            learning_rate=config_json["learning_rate"], 
            update_frequency=update_frequency,
            momentum=bool(config_json["momentum"]), 
            use_adam=False)

            ae.train(training_set, training_set, config_json["epoch_limit"], (lambda e, error, w, o: callback_function(e, error, str(arch), i)))
            for j in range(len(testing_set)):
                labels, x_values, y_values = ae.get_latent_space(testing_set[j])
                with open(f"{base_output_path}latent_{arch}_{i}.txt", 'a') as f:
                    for l, x, y in zip(labels, x_values, y_values):
                        f.write(f"{l},{x},{y},{j}\n")
                f.close()

                test_error = ae.test_autoencoder(testing_set[j])
                with open(f"{base_output_path}avg_error_{arch}.txt", 'a') as f:
                    f.write(f"{i},{test_error},{j}\n")



def callback_function(epoch, error, _input, execution):
    f = open(f"{base_output_path}log_{_input}_{execution}.txt", "a")
    f.write(f"{epoch},{error}\n")
    f.close()


def graph_evolution(execution_number, input_values, comparing_attribute):
    for _in in input_values:
        f = open(f"{base_output_path}log_{_in}_{execution_number}.txt", "r")
        epochs = list()
        errors = list()
        for line in f.readlines():
            epoch, error = line.split(",")
            epochs.append(int(epoch))
            errors.append(float(error))
        f.close()
        plt.plot(epochs, errors, label=_in)
    plt.xlabel("Epoch")
    plt.ylabel("Error")
    plt.legend()
    #save figure
    plt.savefig(f"{base_output_path}err_evolution_{comparing_attribute}_{execution_number}.png")

def graph_latent_space(execution_number, input_values, comparing_attribute):
    for _in in input_values:
        f = open(f"{base_output_path}latent_{_in}_{execution_number}.txt", "r")
        labels = list()
        x_values = list()
        y_values = list()
        classes = list()

        for line in f.readlines():
            l, x, y, c = line.split(",")
            labels.append(l)
            x_values.append(float(x))
            y_values.append(float(y))
            classes.append(int(c))
        f.close()
        plt.scatter(x_values, y_values, label=_in)
        # plt.text(x_values, y_values, labels)
    plt.legend()
    plt.xlabel("dim 1")
    plt.ylabel("dim 2")
    #save figure
    plt.savefig(f"{base_output_path}final_latent_{comparing_attribute}_{execution_number}.png")

def graph_comp_error(input_values, comparing_attribute, execution_count):
    avg_errors = list()
    deviations = list()
    ax = plt.axes()
    for val in input_values:
        f = open(f"{base_output_path}avg_error_{val}.txt", "r")
        errors = list()
        for line in f.readlines():
            epoch, error, c = line.split(",")
            errors.append(float(error))
        f.close()
        avg_errors.append(np.mean(errors))
        deviations.append(np.std(errors))
    plt.scatter(range(len(input_values)), avg_errors)
    plt.errorbar(range(len(input_values)), avg_errors, deviations, marker=".", capsize=5, ecolor='black', elinewidth=1)
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    plt.xticks(range(len(input_values)), input_values)
    plt.xlabel("Architecture")
    plt.ylabel("Error")
    plt.legend()
    #save figure
    plt.savefig(f"{base_output_path}compare_avg_error_{comparing_attribute}.png")