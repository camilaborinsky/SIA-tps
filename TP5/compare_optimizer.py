from parser import parse_config, data_converter, sample_set
from matplotlib import pyplot as plt

import numpy as np

from optimized_autoencoder import OptimizedAutoencoder
base_output_path = "output/optimizers/"
def compare_optimizer():
    
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
        # training_set.append(flattened_input[0])
        training_set.extend(sample_set(flattened_input, config_json["training_sample"]))
        testing_set.append(list(zip(labels, flattened_input)))
    
    latent_dimension = 2
    update_frequency = 0
    execution_count = 5
    input_dimension = len(training_set[0])
    activation_function = (lambda x: 1/(1+np.exp(-2*x)))
    activation_derivative = (lambda x, *args: 2*(1/(1+np.exp(-2*x)))*(1-(1/(1+np.exp(-2*x)))) )
    update_learn_rate=False
    architecture = config_json["architecture"]
    optimizer = config_json["optimizer"]
    learning_rate = config_json["learning_rate"]
    epoch_limit = config_json["epoch_limit"]
    print(len(training_set))

    for o in config_json["optimizers"]:
        with open(f"{base_output_path}avg_train_error_{o}.txt", "w") as error_f:
            with open(f"{base_output_path}avg_test_error_{o}.txt", 'w') as test_error_f:
                for i in range(execution_count):
                    optimized_autoencoder = OptimizedAutoencoder(o, input_dimension, latent_dimension, architecture, activation_function, activation_derivative)
                    final_error, errors = optimized_autoencoder.train(training_set, training_set, epoch_limit)

                    with open(f"{base_output_path}log_{o}_{i}.txt", "w") as f:
                        for k in range(len(errors)):
                            f.write(f"{k},{errors[k]}\n")
                    f.close()
                    error_f.write(f"{i},{final_error}")

                    with open(f"{base_output_path}latent_{o}_{i}.txt", 'w') as f:
                        for j in range(len(testing_set)):
                            labels, x_values, y_values = optimized_autoencoder.get_latent_space(testing_set[j])
                        
                            for l, x, y in zip(labels, x_values, y_values):
                                f.write(f"{l},{x},{y},{j}\n")
                    f.close()
                   

                    test_error = optimized_autoencoder.test_autoencoder(testing_set[j])
                
                    test_error_f.write(f"{i},{test_error},{j}\n")
            test_error_f.close()
        error_f.close()


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
    #which_font should be -1 if we want to graph all fonts, otherwise it should be the index of the font we want to graph
    for _in in input_values:
        f = open(f"{base_output_path}latent_{_in}_{execution_number}.txt", "r")
        labels = list()
        x_values = list()
        y_values = list()
        classes = list()

        for line in f.readlines():
            l, x, y, c = line.split(",")
            x_values.append(float(x))
            y_values.append(float(y))
            classes.append(int(c))
            labels.append(str(l))
        f.close()
        plt.scatter(x_values, y_values, label=_in)
        #plt.text(x_values, y_values, str(labels))
    plt.legend()
    plt.xlabel("dim 1")
    plt.ylabel("dim 2")
    #save figure
    plt.savefig(f"{base_output_path}final_latent_{comparing_attribute}_{execution_number}.png")


def graph_latent_space_BFGS(execution_number, input_values, comparing_attribute):
    f = open(f"{base_output_path}latent_BFGS_{execution_number}.txt", "r")
    labels = list()
    x_values = list()
    y_values = list()
    classes = list()

    for line in f.readlines():
        l, x, y, c = line.split(",")
        x_values.append(float(x))
        y_values.append(float(y))
        classes.append(int(c))
        labels.append(str(l))
    f.close()
    #scatterplot with orange color
    plt.scatter(x_values, y_values, c="orange", label="BFGS")
    #plt.text(x_values, y_values, str(labels))
    plt.legend()
    plt.xlabel("dim 1")
    plt.ylabel("dim 2")
    #save figure
    plt.savefig(f"{base_output_path}final_latent_{comparing_attribute}_{execution_number}.png")


def graph_comp_error_test(input_values, comparing_attribute, execution_count):
    avg_errors = list()
    deviations = list()

    ax = plt.axes()
    for val in input_values:
        print("val: ", str(val))
        f = open(f"{base_output_path}avg_test_error_{val}.txt", "r")
        g = open(f"{base_output_path}avg_train_error_{val}.txt", "r")
        errors = list()
        train_errors = list()
        for line in f.readlines():
            epoch, error, last = line.split(",")
            errors.append(float(error))
        f.close()
        for line in g.readlines():
            epoch, error, last = line.split(",")
            train_errors.append(float(error))
        g.close()

        avg_errors.append(np.mean(errors))
        deviations.append(np.std(errors))

        avg_errors_train = np.mean(train_errors)
        deviations_train = np.std(train_errors)

    plt.scatter(range(len(input_values)), avg_errors, label=comparing_attribute)
    plt.errorbar(range(len(input_values)), avg_errors, deviations)
    plt.scatter(range(len(input_values)), avg_errors_train, label="Training")
    plt.errorbar(range(len(input_values)), avg_errors_train, deviations_train)

    plt.legend()
    plt.xlabel("Optimizer")
    plt.get_xaxis().set_visible(False)
    plt.ylabel("Average Error")
    #save figure
    plt.savefig(f"{base_output_path}avg_train_error_{comparing_attribute}.png")