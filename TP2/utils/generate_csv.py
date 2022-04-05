import csv


def generate_csv_file(filename, data):
    f = open(filename, "w")
    writer = csv.writer(f)
    for t in enumerate(data):
        row = t[1]
        writer.writerow([row.generation_number, row.mean_fitness, row.max_fitness, row.min_fitness, row.gen_diversity, row.fit_diversity])

    f.close()

def average_csv_files(files_for_avg, file_count, generation_count):
    files =[None]*file_count
    readers = [None]*file_count
    output_file = open(f"output/average/{files_for_avg}_avg.csv", "w")
    writer = csv.writer(output_file)
    for i in range(file_count):
        files[i] = open(f"output/raw/{files_for_avg}_{i}.csv")
        readers[i] = list(csv.reader(files[i], delimiter=","))
    print(generation_count)
    for row in range(generation_count):
        sums = [0]*(len(readers[0][0])-1)
        for j in range(len(readers)):
            for i in range(len(sums)):
                # print(f"row: {row}, j:{j}, i:{i}, lencsv:{len(readers[j][row])}")
                sums[i]+= float(readers[j][row][i+1])

        for t in range(len(sums)):
            print(type(sums[t]))
        new_list = map(lambda x: x/generation_count, sums)
        writer.writerow(list(new_list))
    for i in range(0, file_count):
        files[i].close()
    output_file.close()


