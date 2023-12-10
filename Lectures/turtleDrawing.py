import turtle
import math

# print("Please enter the length of each side.")
# side_len = int(input())
#
# turtle.forward(side_len)
# turtle.right(90)
#
# turtle.forward(side_len)
# turtle.right(90)
#
# turtle.forward(side_len)
# turtle.right(90)
#
# turtle.forward(side_len)
# turtle.right(90)
#
# turtle.hideturtle()
# turtle.done()

print("Great Now lets draw a right triangle")
side1 = float(input("Enter the length of side 1:"))
side2 = float(input("Enter the length of side 2:"))
side3 = math.sqrt(side1**2 + side2**2)

alpha = math.degrees(math.atan(side1/side2))
beta = 90 - alpha


turtle.forward(side1)
turtle.left(90)
turtle.forward(side2)
turtle.left(180 - alpha)
turtle.forward(side3)
turtle.left(180 - beta)

turtle.hideturtle()
turtle.done()
