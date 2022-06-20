
import json

import numpy as np
from visualize_letters import print_letter


def data_converter(file_path):
    with open(file_path) as f:
        characters = list()
        labels = list()
        for current_line in f.readlines():
            current_line = current_line.strip()
            current_line = current_line.replace('{', '', 1).replace('}', '', 1)
            values = []
            values = current_line.split(',')
            binaries = []
            for h in values[:-1]:
                bins = bin(int(h, 16))[2:].zfill(5)
                binaries.append([int(b) for b in bins])
            characters.append(binaries)
            labels.append(values[-1])
    f.close()

    return labels, characters


def parse_config(file_path):
    with open(file_path) as f:
       config = json.load(f)
    f.close()
    return config

def sample_set(element_set, fraction):
    sample_size = int(len(element_set) * fraction)
    #return random sample of element_set of size sample_size
    indexes = np.random.choice(len(element_set), sample_size, replace=False)
    return np.array([element_set[i] for i in indexes])
