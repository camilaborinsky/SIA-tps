import matplotlib.pyplot as plt
import numpy as np


def parser_letters(path_to_file):
    print("Enter parser")
    all_letters = []
    matrix = []
    with open(path_to_file) as f:
        counter = 0
        for current_line in f: 
            current_line = current_line.strip()
            if counter % 5 == 0 and counter != 0:
                all_letters.append(matrix)
                matrix = []
                count = 0
            
            counter += 1
            a,b,c,d,e = current_line.split(",")
            matrix.append([a,b,c,d,e])
    f.close()
    all_letters.append(matrix)
    print(str(all_letters))
    return all_letters




def letters_with_asterisks(all_letters_matrix):
    print(str(all_letters_matrix))
    for letter in all_letters_matrix:
        for row in letter:
            for item in row: 
                if item == '1':
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print("\n")
        print("\n")


def print_letter(letter_as_binary_matrix):
    plt.figure(figsize=(1,1))
    plt.imshow(letter_as_binary_matrix, cmap='Greys')
    plt.show()


def add_noise_to_letter(letter_as_binary_matrix, noise_level):
    noisy_letter = np.zeros(letter_as_binary_matrix.shape)
    for i in range(len(letter_as_binary_matrix)):
        for j in range(len(letter_as_binary_matrix[i])):
            a = np.random.random()
            if a < noise_level:
                if letter_as_binary_matrix[i][j] == 1:
                    noisy_letter[i][j] = 0
                else: 
                    noisy_letter[i][j] = 1
            else:
                noisy_letter[i][j] = letter_as_binary_matrix[i][j]
    return noisy_letter


def generate_noisy_samples(letter_as_bin_matrix, sample_size, noise_level):
    noisy_samples = []
    for i in range(sample_size):
        # print(letter_as_bin_matrix)
        new_letter = add_noise_to_letter(letter_as_bin_matrix, noise_level)
        noisy_samples.append(new_letter)
    
    return noisy_samples