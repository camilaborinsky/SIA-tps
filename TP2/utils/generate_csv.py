import csv


def generate_csv_file(filename, data):
    f = open(filename, "w")
    writer = csv.writer(f)
    print(type(data))
    for t in enumerate(data):
        row = t[1]
        writer.writerow([row.generation_number, row.mean_fitness, row.max_fitness, row.min_fitness])

    f.close()

