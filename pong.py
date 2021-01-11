import turtle


def run():
    win = turtle.Screen()
    win.title("Pong by @abhinav.robinson")
    win.bgcolor("black")
    win.setup(width=800, height=600)
    win.tracer(0)

    while True:
        win.update()


class Paddle(turtle.Turtle):

    def __init__(self, xcor, ycor):
        self = turtle.Turtle()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xcor, ycor)


class Ball(turtle.Turtle):

    def __init__(self):
        self = turtle.Turtle()
        self.speed(0)
        self.shape("square")
        self.color("white")

        self.penup()
        self.goto(0, 0)


def createGameObjects():

    # ADD PADDLE A
    pd_a = Paddle(-350, 0)
    
    # ADD PADDLE B
    pd_b = Paddle(350, 0)

    # ADD BALL
    ball = Ball()

    # MOVE PADDLES


# START GAME LOOP
def main():
    createGameObjects()

    run()


main()
