def main():
    file_name = input("Enter the name of the text file: ")
    
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            print("File contents:")
            print(file_content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{file_name}'.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
