from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def reset():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="d", fun=move_right)
screen.onkey(key="c", fun=reset)
screen.exitonclick()