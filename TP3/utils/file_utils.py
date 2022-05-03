
import numpy as np


def parse_training_set_from_file(file_path):
    training_set = []
    expected_output = []
    with open(file_path+"/training.txt") as f:
        for line in f:
            training_set.append([float(item) for item in line.strip().split()])
    f.close()
    with open(file_path+"/expected.txt") as f:
        for line in f:
            expected_output.append([float(item) for item in line.strip().split()])
    f.close()
    

    return training_set, expected_output


def generate_linear_training(file_path, eq_nr):
    solution = np.random.uniform(-10, 10, eq_nr)
    with open(file_path + "/training.txt", "w") as f1:
        with open(file_path + "/expected.txt", "w") as f2:
            with open(file_path + "/solution.txt", "w") as f3:
                for idx in range(eq_nr):
                    aux_eq = np.random.uniform(size=eq_nr)
                    f1.write("\t"+'\t'.join(map(lambda i : str(i), aux_eq))+ "\t\n")
                    f2.write("\t"+str(np.dot(aux_eq, solution))+ "\t\n")
                f3.write("\t"+str(solution)+ "\t\n")
                f3.close()
            f2.close()
        f1.close()

def write_error_vs_iteration(file_path, error, iteration):
    with open(file_path + "/error_vs_iteration.txt", "a") as f:
        f.write(str(iteration)+","+str(error)+"\n")
    f.close()
    
def generate_parity_output(file_path ):
    with open(file_path + "/training.txt", "r") as f1:
        with open(file_path + "/expected.txt", "w") as f2:
            for line in f1:
                if line.strip().split()[-1] == 0:
                    parity = 1
                else:
                    parity = -1
                f2.write("\t"+str(parity)+"\t\n")
            f2.close()
        f1.close()

    