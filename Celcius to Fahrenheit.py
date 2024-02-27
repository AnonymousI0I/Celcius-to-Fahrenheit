# Define a function for decimal addition
def decimal_addition(num1, num2):
    return num1 + num2

# Define a function for simple interest calculation
def calculate_simple_interest(principal, rate, time):
    simple_interest = principal * rate * time
    return simple_interest

# Define a function for Celsius to Fahrenheit conversion
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

# Main function implementation
def main():
    # Decimal Addition
    decimal1 = float(input("Enter the first floating-point number: "))
    decimal2 = float(input("Enter the second floating-point number: "))
    sum_result = decimal_addition(decimal1, decimal2)
    print(f"Sum of {decimal1} and {decimal2} is {sum_result}")

    # Simple Interest Calculation
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (e.g., 0.01): "))
    time = float(input("Enter the time (in years): "))
    interest_result = calculate_simple_interest(principal, rate, time)
    print(f"Simple Interest for the provided details is: {interest_result}")

    # Celsius to Fahrenheit Conversion
    celsius_degree = float(input("Enter the temperature in Celsius: "))
    fahrenheit_result = celsius_to_fahrenheit(celsius_degree)
    print(f"{celsius_degree} Celsius is equal to {fahrenheit_result} Fahrenheit")

# Call the main function
if __name__ == "__main__":
    main()
