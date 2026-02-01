height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100) ** 2
print("Your BMI is:", round(BMI, 2))
if BMI <= 18.5:
    print("You are underweight.")
elif 18.5 <= BMI < 24.9:
    print("normal weight.")
elif 25 <= BMI < 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are obese class I.")
elif BMI <= 39.9:
    print("You are obese class II.")
else:
    print("You are severly obese.")
