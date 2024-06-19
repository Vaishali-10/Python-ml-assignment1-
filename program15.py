import csv

def read_csv_file(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{file_path}'.")

# Example usage:
file_path = 'data.csv'
print(f"Reading data from '{file_path}':")
read_csv_file(file_path)
