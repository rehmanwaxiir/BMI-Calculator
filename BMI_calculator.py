"""
BMI Calculator is a simple program that calculates a person's Body Mass Index (BMI) using their weight and height.
"""
print("===BMI calculator===")
try:
    weight=float(input("Please enter your weight in kg."))
    height=float(input("Please enter your height in meter."))
    if weight<=0 or height<=0:
        print("weight and height must be greater then zero.")
    else:
        bmi=weight/(height**2)
        print(f"your bmi is {bmi:2f}.")
    if bmi<18.5:
        print("category: under weight.")
    elif bmi<25:
        print("category: healthy weight.")
    elif bmi< 30:
        print("category: over weight.")
    else:
        print("category: obesity.")
except ValueError:
    print("Please enter a valid bmi numbers.")            
