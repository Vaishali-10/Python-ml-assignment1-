def sum_of_digits(number):
    # Initialize sum to 0
    sum_digits = 0
    
    # Iterate over each digit in the number
    while number > 0:
        # Add the last digit to sum
        sum_digits += number % 10
        # Remove the last digit from number
        number //= 10
    
    return sum_digits

# Example usage:
num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"The sum of the digits of {num} is: {result}")
