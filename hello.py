def is_armstrong(number):
    # Convert the number to a string to find its length and digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = 0
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    
    # Check if the sum equals the original number
    return sum_of_powers == number

# Get input from the user
num = int(input("Enter a number to check if it's an Armstrong number: "))

# Check and display the result
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")