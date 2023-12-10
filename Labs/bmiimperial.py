'''
BMI Imperial Lab:

Description

Body  mass  index (BMI) is  a number  calculated  from  a person’s weight and height. According to the Centers for Disease Control and Prevention, the BMI is a fairly reliable indicator of body fatness for most people. BMI does not measure body fat directly, but research  has shown that  BMI correlates  to  direct  measures  of  body  fat, such  as  underwater  weighing  and dual-energy X-ray absorptiometry. The formula for BMI is Weight/Height2 where weight is in kilograms and height is in meters.

Write a program that prompts for weight in pounds and height in inches, converts the values to metric, and then calculates the BMI.
Note: 1 pound is 0.453592 kilograms and 1 inch is 0.0254 meters.


For example, an execution could look like this:

   Please enter weight in pounds: 135
   Please enter height in inches: 71
   BMI is: 18.8284697141
'''

print("We will calculate BMI based on a given weight and height:")
weight = float(input("Please enter weight in pounds: ")) * 0.453592
height = float(input("Please enter height in inches: ")) * 0.0254

bmi = weight / (height ** 2)
print("BMI is:", bmi)
