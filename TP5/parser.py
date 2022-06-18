
from visualize_letters import print_letter


def data_converter(file_path):
    with open(file_path + "/fonts.txt") as f:
        characters = list()
        for current_line in f.readlines():
            current_line = current_line.strip()
            current_line = current_line.replace('{', '').replace('}', '')
            values = []
            values = current_line.split(',')
            binaries = []
            # print(str(values))
            for h in values:
                bins = bin(int(h, 16))[2:].zfill(5)
                binaries.append([int(b) for b in bins])
                # print(str(bins))
            characters.append(binaries)
    f.close()

    return characters
    # print_letter(characters[4])
# data_converter("resources")