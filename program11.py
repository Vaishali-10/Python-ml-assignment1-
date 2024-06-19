def fibonacci_sequence(n):
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate Fibonacci sequence
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence[:n]

# Example usage:
num_terms = int(input("Enter the number of Fibonacci numbers to generate: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_numbers = fibonacci_sequence(num_terms)
    print(f"The first {num_terms} Fibonacci numbers are: {fibonacci_numbers}")
