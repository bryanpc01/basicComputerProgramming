import turtle


def main():
    num_of_squares = int(input("Please enter the number of squares you wish to draw: "))

    turtle_fan_of_squares(num_of_squares, 100)
    turtle.hideturtle()
    turtle.done()


def turtle_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)


def turtle_fan_of_squares(number_of_squares, side_length):
    for _ in range(number_of_squares):
        turtle_square(side_length)
        turtle.left(360 / number_of_squares)


main()
