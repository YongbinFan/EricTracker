from turtle import Turtle, Screen

aim = Turtle()
aim.shape("triangle")
aim.color("red")
aim.shapesize(stretch_wid=0.5, stretch_len=0.5)
aim.penup()
screen = Screen()
screen.bgpic('background.png')
screen.update()
screen.setup(500, 400)
is_int = False
while not is_int:
    try:
        projectiles = int(input("How many missiles do you want to send?"))
    except ValueError:
        pass


def up():
    aim.setheading(90)
    aim.forward(20)


def down():
    aim.setheading(270)
    aim.forward(20)


def left():
    aim.setheading(180)
    aim.forward(20)


def right():
    aim.setheading(0)
    aim.forward(20)


def deploy():
    aim.dot(25, (0, 0, 0))


screen.listen()

screen.onkey(up, "w")  # This will call the up function if the "W" arrow key is pressed
screen.onkey(down, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(deploy, "e")

screen.mainloop()
