
# Python BMI Calculator

A simple command-line BMI Calculator developed using Python. The program asks the user for their weight in kilograms and height in meters, calculates their Body Mass Index (BMI), and displays the corresponding adult BMI category.

## Features

- Accepts weight in kilograms.
- Accepts height in meters.
- Calculates BMI using the standard formula.
- Displays BMI rounded to two decimal places.
- Categorizes BMI using adult screening ranges.
- Validates positive weight and height.
- Handles invalid numeric input.

## BMI Formula

BMI is calculated using:

BMI = Weight (kg) / Height (m)²

## Adult BMI Categories

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 to below 25 | Healthy weight |
| 25 to below 30 | Overweight |
| 30 or above | Obesity |

These are general adult screening categories, not a medical diagnosis. BMI is interpreted differently for children and teenagers.

## Requirements

- Python 3
- No external libraries required

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Run the program in the terminal:

   ```bash
   python bmi_calculator.py
   ```

   On Windows, you can also use:

   ```bash
   py bmi_calculator.py
   ```

4. Enter your weight in kilograms.
5. Enter your height in meters.
6. View your BMI result and category.

## Python Concepts Used

- Variables and data types
- User input and output
- Type conversion using `float()`
- Arithmetic operators
- Conditional statements (`if`, `elif`, `else`)
- Exception handling (`try`, `except`)
- Formatted strings

## Project Type

Beginner-friendly Python command-line application.

## Author

Rehman Ullah
