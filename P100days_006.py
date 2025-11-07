import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return (r, g, b)

def spirograph(gap):
    steps = int(360/gap+1)
    angle = 0
    for i in range (steps):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(angle)
        angle += gap

t.colormode(255)

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

screen = t.Screen()


# #challenge 1
for i in range(4):
    tim.forward(100)
    tim.right(90)

# # #challenge 2
for i in range (15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# # #challenge 3
sides = 3
while sides <= 10:
    angle = 360/sides
    tim.color(random_color())
    for i in range (sides):
        tim.forward(100)
        tim.rt(angle)
    sides += 1


# # #challenge 4
tim.speed("fastest")
tim.pensize(10)
count = 0
while count < 200:
    angle = 90*random.randint(0,3)
    tim.color(random_color())
    tim.setheading(angle)
    tim.forward(30)
    count += 1

# #challenge 5
tim.speed("fastest")
tim.pensize(1)
spirograph(3.6)

        
screen.exitonclick()