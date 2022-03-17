# Getting the height and weight details from user
height = float(input("enter your height in foot: "))
weight = float(input("enter your weight in kg: "))

# Formula for BMI Calculator
bmi = weight / ((height * 0.305) ** 2)

# According to BMI giving the description to the user
if bmi < 18.5:
    print(f"Your BMI is {round(bmi)}, you are underweight.")
elif (bmi > 18.5) and (bmi < 25):
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif (bmi > 25) and (bmi < 30):
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif (bmi > 30) and (bmi < 35):
    print(f"Your BMI is {round(bmi)}, you are obese.")
elif bmi > 35:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")
