from Utils.GenerateDataset import read_and_clean_csv_data, generate_location_objects

if __name__ == "__main__":
    x = read_and_clean_csv_data()
    generate_location_objects(x)