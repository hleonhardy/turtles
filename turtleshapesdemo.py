import turtle

# opens a window to draw on
window = turtle.Screen()
# makes the window white
window.bgcolor("white")


def draw_square(new_turtle):
    for x in range(0, 4):
        new_turtle.pendown()
        new_turtle.right(90)
        new_turtle.forward(100)


def draw():
    # create an instance of Turtle
    jane = turtle.Turtle()

    # set values on attributes in the Turtle module
    jane.shape("turtle")
    jane.color("green", "yellow")  # outline color, fill color
    jane.penup()
    jane.setx(150)

    # # create another instance of Turtle and set its values
    # ginger = turtle.Turtle()
    # ginger.shape("classic")
    # ginger.color("blue", "purple")
    # ginger.penup()
    # ginger.setx(-150)

    # draw one square filled with color with the jane instance
    jane.begin_fill()
    draw_square(jane)
    jane.end_fill()


    terry = turtle.Turtle()
    terry.shape("turtle")
    terry.color("red", "pink")
    terry.penup()
    terry.setx(-10)
    terry.sety (100)
    terry.begin_fill()


    terryJr = turtle.Turtle()
    terryJr.shape("turtle")
    #hot pink hopefully
    terryJr.color("#FF69B4","#32CD32")
    terryJr.penup()
    terryJr.setx(-150)
    terryJr.stamp()

    terryJr.begin_fill()

    for x in range(0,15):
        terryJr.pendown()
        terryJr.circle(50,180)
        terryJr.stamp()
        terryJr.circle(50,180)
        terryJr.right(30)
        


    terryJr.end_fill()



    for x in range(0,5):
        terry.pendown()
        terry.forward(50)
        terry.right(144)

    terry.end_fill()


    # ginger.begin_fill()
    # for x in range(0, 36):
    # # draw offset squares in a loop with the ginger instance

    #     draw_square(ginger)
    #     ginger.right(10)

    # ginger.end_fill()

    window.exitonclick()

# Sometimes we only want code to run if we are running this file directly.
# If we were to import this file, we wouldn't necessarily want our functions to
# run.
# By using the following conditional the draw function will not be called unless
# we run this file directly -- by calling `python turtleshapesdemo.py`
# Want to learn more about if __name__ == '__main__':?
# Check out:
# http://stackoverflow.com/a/20158605 and/or
# https://www.youtube.com/watch?v=sugvnHA7ElY
if __name__ == '__main__':
    draw()