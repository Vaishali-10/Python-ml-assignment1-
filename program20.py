def calculate_sum(numbers):
    total = sum(numbers)
    return total

# Example usage:
try:
    # Input list of numbers separated by spaces
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = list(map(float, numbers))  # Convert input strings to floats
    
    # Calculate the sum of numbers
    total_sum = calculate_sum(numbers)
    
    # Print the sum
    print(f"The sum of the numbers is: {total_sum}")

except ValueError:
    print("Invalid input. Please enter valid numbers separated by spaces.")
