'''
BMI Metric With Status Category Lab:

Description

Modify your earlier BMI Metric program to round to two decimal positions and also display the CDC standard weight status categories:

The CDC standard weight status categories are:

BMI -> Weight Status

Below 18.5 -> Underweight

18.5-24.9 -> Normal

25.0-29.9 -> Overweight

30.0 and above -> Obese

For example, an execution could look like this:

Please enter weight in kilograms: 50
Please enter height in meters: 1.58
BMI is: 20.03, Status is Normal
'''

print("We will calculate BMI based on a given weight and height:")
weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))

bmi = round(weight / (height ** 2),2)

if (bmi < 18.5):
    status = "Underweight"
elif (18.5 <= bmi < 25):
    status = "Normal"
elif (25 <= bmi < 30):
    status = "Overweight"
elif (bmi >= 30):
    status = "Obese"
else:
    status = "Undefined"
print(f"BMI is: {bmi}, Status is {status}.")
