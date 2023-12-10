'''
BMI Metric Lab:

Description

Body mass index (BMI) is a number calculated from a person’s weight and height. According to the Centers for Disease
Control and Prevention, the BMI is a fairly reliable indicator of body fatness for most people. BMI does not measure body fat directly, but research has shown that BMI correlates to direct measures of body fat, such as underwater weighing and dual-energy X-ray absorptiometry. The formula for BMI is Weight/Height^2 where weight is in kilograms and height is in meters.

Write a program that prompts for metric weight and height and outputs the BMI.


For example, an execution could look like this:

   Please enter weight in kilograms: 50
   Please enter height in meters: 1.58
   BMI is: 20.0288415318
'''

print("We will calculate BMI based on a given weight and height:")
weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))

bmi = weight / (height ** 2)
print("BMI is:", bmi)
