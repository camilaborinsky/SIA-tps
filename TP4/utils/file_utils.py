import numpy as np


def parse_countries_data(data_file_path):
    f = open(data_file_path)
    lines = f.readlines()
    data = [None]*(len(lines)-1)
    countries = [None]*(len(lines)-1)
    for i,line in enumerate(lines):
        if i == 0:
            continue
        data[i-1] = [float(x) for x in line.split(",")[1:]]
        countries[i-1] = line.split(",")[0][1:-1]
    attributes = [att[1:-1] for att in lines[0].strip().split(",")[1:]]

    f.close()
    return attributes, countries, data


def standarize_data(data):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    return (data - mean)/std


