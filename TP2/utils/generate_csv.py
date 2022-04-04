import csv


def generate_csv_file(filename, data):
    f = open(filename)
    writer = csv.writer(f)
    for row in enumerate(data):
        writer.writerow([row.generation_number, row.mean_fitness, row.max_fitness, row.min_fitness])

    f.close()