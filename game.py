import turtle


win = turtle.Screen()
win.title("Pong by @abhinav.robinson")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


# START GAME LOOP
def main():
    while True:
        win.update()


main()
