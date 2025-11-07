import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    rgb = (r, g, b)
    return rgb

t.colormode(255)

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")

screen = t.Screen()


#challenge 1
for i in range(4):
    timmy.forward(100)
    timmy.right(90)

# #challenge 2
for i in range (15):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

# #challenge 3
sides = 3
timmy.pendown()
while sides <= 10:
    angle = 360/sides
    timmy.color(random_color())
    for i in range (sides):
        timmy.forward(100)
        timmy.rt(angle)
    sides += 1


# #challenge 4
timmy.speed("fastest")
timmy.pensize(10)
count = 0
while count < 1000:
    angle = 90*random.randint(0,3)
    timmy.color(random_color())
    timmy.right(angle)
    timmy.forward(30)
    count += 1

# #challenge 5
timmy.speed("fastest")
timmy.pensize(1)
steps = 36
angle = 360 / steps
for i in range (steps):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.rt(angle)
        
screen.exitonclick()