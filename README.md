# Utility Functions in Python

This Python script provides a collection of utility functions for various calculations and conversions. The main functionalities include:

1. Decimal Addition
2. Simple Interest Calculation
3. Celsius to Fahrenheit Conversion

## Features

- **Decimal Addition**: Add two floating-point numbers.
- **Simple Interest Calculation**: Calculate the simple interest given the principal, rate of interest, and time.
- **Celsius to Fahrenheit Conversion**: Convert a temperature from Celsius to Fahrenheit.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/utility-functions.git
    cd utility-functions
    ```

2. **Ensure Python 3.x is installed on your machine**.

## Usage

1. **Run the script**:

    ```bash
    python utility_functions.py
    ```

2. **Follow the on-screen prompts to use the different functionalities**:

### Decimal Addition

- You will be prompted to enter two floating-point numbers.
- The program will display the sum of the two numbers.

    Example:

    ```
    Enter the first floating-point number: 5.5
    Enter the second floating-point number: 3.2
    Sum of 5.5 and 3.2 is 8.7
    ```

### Simple Interest Calculation

- You will be prompted to enter the principal amount, rate of interest (as a decimal), and time (in years).
- The program will display the calculated simple interest.

    Example:

    ```
    Enter the principal amount: 1000
    Enter the rate of interest (e.g., 0.01): 0.05
    Enter the time (in years): 3
    Simple Interest for the provided details is: 150.0
    ```

### Celsius to Fahrenheit Conversion

- You will be prompted to enter the temperature in Celsius.
- The program will display the equivalent temperature in Fahrenheit.

    Example:

    ```
    Enter the temperature in Celsius: 25
    25.0 Celsius is equal to 77.0 Fahrenheit
    ```

## Code Overview

### Function Descriptions

#### `decimal_addition(num1, num2)`

Adds two floating-point numbers and returns the result.

- **Parameters**:
  - `num1` (float): The first number.
  - `num2` (float): The second number.
- **Returns**:
  - `float`: The sum of `num1` and `num2`.

#### `calculate_simple_interest(principal, rate, time)`

Calculates simple interest based on the given principal, rate, and time.

- **Parameters**:
  - `principal` (float): The initial amount of money.
  - `rate` (float): The rate of interest (e.g., 0.01 for 1%).
  - `time` (float): The time the money is invested or borrowed for, in years.
- **Returns**:
  - `float`: The calculated simple interest.

#### `celsius_to_fahrenheit(celsius)`

Converts a temperature from Celsius to Fahrenheit.

- **Parameters**:
  - `celsius` (float): The temperature in Celsius.
- **Returns**:
  - `float`: The temperature in Fahrenheit.

### Main Function

The `main()` function orchestrates the workflow by prompting the user for inputs, calling the respective functions, and displaying the results. It covers:

- Adding two decimal numbers.
- Calculating simple interest.
- Converting Celsius to Fahrenheit.

## Contribution

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.
