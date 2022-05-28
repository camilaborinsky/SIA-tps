
def parser_letters2(path_to_file):
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


def parser_letters(path_to_file):
    all_letters = [] #list of all the matrixes of letters
    with open(path_to_file) as f: 
        #read matrix of 5x5
        current_line = f.readline().strip()
        matrix = []
        count = 0
        while current_line != "\n":
            #Reinicio el counter de lineas cuando ya levante 5. Salteo el nombre de la letra y el enter
            if count % 5 == 0 and count != 0:
                all_letters.append(matrix)
                matrix = []
                count = 0

            print(current_line)
            count +=1
            a,b,c,d,e = current_line.split(",")
            matrix.append([a,b,c,d,e])
            current_line = f.readline().strip()

    f.close()
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


letters_with_asterisks(parser_letters2("TP4/ex_2/resources/letters.txt"))