Height = float(input("Enter your height in meters: "))
Weight = float(input("Enter your weight in kilograms: "))
Height = Height / 100
BMI = Weight / (Height * Height)
print("Your BMI is: ", BMI)
if (BMI > 0):
    if (BMI < 16):
        print("You are severely underweight")
    elif (BMI > 18.5 and BMI < 25):
        print("You are healthy")
    elif (BMI > 25 and BMI < 30):
        print("You are overweight")
    elif (BMI > 30):
        print("You are obese")
    else:
        print("You are not healthy")
else:
    print("Invalid Input")
