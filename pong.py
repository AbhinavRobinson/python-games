import turtle


class getWindow(turtle.Turtle):

    window = None

    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Pong by @abhinav.robinson")
        self.window.bgcolor("black")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)

    def run(self):
        while True:
            self.window.update()


class Paddle(turtle.Turtle):
    xcor, ycor = 0, 0

    def __init__(self, xcor, ycor):
        self = turtle.Turtle()
        self.speed(0)
        self.shape("square")
        self.color("white")

        self.shapesize(stretch_wid=5, stretch_len=1)

        self.penup()
        self.goto(xcor, ycor)

        self.xcor = self.xcor()
        self.ycor = self.ycor()

    def move(self, mag):
        self.sety(self.ycor+(20*mag))


class Ball(turtle.Turtle):
    xcor, ycor = 0, 0

    def __init__(self):
        self = turtle.Turtle()
        self.speed(0)
        self.shape("square")
        self.color("white")

        self.penup()
        self.goto(0, 0)

        self.xcor = self.xcor()
        self.ycor = self.ycor()


def createGameObjects():
    # ADD PADDLE A
    pd_a = Paddle(-350, 0)

    # ADD PADDLE B
    pd_b = Paddle(350, 0)

    # ADD BALL
    ball = Ball()


# def actionHandler(self):
#     win.

# START GAME LOOP


def main():
    win = getWindow()

    createGameObjects()

    win.run()


main()
