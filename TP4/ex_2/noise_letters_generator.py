import random
from TP4.ex_2.visualize_letters import parser_letters
from TP4.ex_2.visualize_letters import letters_with_asterisks

def generate_letters_with_noise(all_letters_matrix, noise_percentage, path_to_noise_file):
    new_letters = []
    new_matrix = []
    new_line = []

    #Clear previous contents of file
    open(path_to_noise_file, 'w').close()

    
    for letter in all_letters_matrix:
        for row in letter:
            for item in row: 
                #generate a random number, if it is less than the noise percentage, change the item from -1 to 1 or vice versa
                if random.randint(0,100) < noise_percentage:
                    if item == '1':
                        new_line.append('-1')
                    else:
                        new_line.append('1')
                else:
                    new_line.append(item)
            new_matrix.append(new_line)
            new_line = []
        new_letters.append(new_matrix)
        new_matrix = []
    
    #Write new contents to file
    with open(path_to_noise_file, 'w') as f:
        for letter in new_letters:
            for row in letter:
                for item in row:
                    f.write(str(item) + ",")
                f.write("\n")
    f.close()
    return new_letters
    

    
letters_with_asterisks(generate_letters_with_noise(parser_letters("TP4/ex_2/resources/letters.txt"), 10, "TP4/ex_2/resources/noise_letters.txt"))
