from utils.file_utils import parse_countries_data, standarize_data


def main():
    attributes, countries, dataset = parse_countries_data("ex_1/resources/europe.csv")
    print(f"rows {len(dataset)}")
    print(f"cols {len(dataset[0])}")
    std = standarize_data(dataset)
    print(f"rows {len(std)}")
    print(f"cols {len(std[0])}")

main()