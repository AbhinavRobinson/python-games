import turtle


win = turtle.Screen()
win.title("Pong by @abhinav.robinson")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


# ADD PADDLE A
pd_a = turtle.Turtle()
pd_a.speed(0)
pd_a.shape("square")
pd_a.color("white")
pd_a.shapesize(stretch_wid=5, stretch_len=1)

pd_a.penup()
pd_a.goto(-350, 0)

# ADD PADDLE B
pd_b = turtle.Turtle()
pd_b.speed(0)
pd_b.shape("square")
pd_b.color("white")
pd_b.shapesize(stretch_wid=5, stretch_len=1)

pd_b.penup()
pd_b.goto(350, 0)

# ADD BALL

# START GAME LOOP


def main():
    while True:
        win.update()


main()
