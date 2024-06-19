def read_lines_until_empty():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    
    return lines

# Example usage:
print("Enter multiple lines of text. Press Enter on an empty line to finish.")
input_lines = read_lines_until_empty()

if input_lines:
    print("\nThe lines you entered:")
    for line in input_lines:
        print(line)
else:
    print("No lines entered.")
