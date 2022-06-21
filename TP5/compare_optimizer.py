from parser import parse_config, data_converter, sample_set
from platform import architecture
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
                        for i in range(len(errors)):
                            f.write(f"{i},{errors[i]}\n")
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

            