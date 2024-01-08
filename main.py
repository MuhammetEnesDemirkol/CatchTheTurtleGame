import turtle
import random

#veriables
gameOver = False
score = 0

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Catch TheTurtle")
screen.bgcolor("light grey")
FONT = ('Arial', 24, 'normal')


#score turtle
scoreTurtle = turtle.Turtle()

#countdown turtle
countdownTurtle=turtle.Turtle()

#turtleList
turtleList = []

#make turtle properties
gridSize = 15
xCoordinates = [-20, -10, 0, 10, 20]
yCoordinates = [-20, -10, 0, 10, 20]

#scoreTable
def setup_score_turtle():
    scoreTurtle.penup() #We do not want a line to be drawn.
    scoreTurtle.hideturtle()#We do not want to see the image icon.
    scoreTurtle.color("black")

    top_width = screen.window_width() / 2
    top_height = screen.window_height() / 2
    #We take half of the total length since we start from the center of the screen.

    y = top_height * 0.9
    x = top_width * 0.8

    scoreTurtle.setposition(x, y)
    scoreTurtle.write(arg="Score: 0", move=False, align="center", font=FONT)

def make_turtle(x, y):

    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        scoreTurtle.clear()
        scoreTurtle.write(arg=f"Score: {score}", move=False, align="center",font=FONT)

    t.shape("turtle")
    t.penup()
    t.shapesize(2, 2)
    t.color("dark green")
    t.goto(x * gridSize, y * gridSize)
    turtleList.append(t)
    t.onclick(handle_click)

def setup_turtles():
    for x in xCoordinates:
        for y in yCoordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtleList:
        t.hideturtle()

def show_turtles_randomly():
    if not gameOver:
        hide_turtles()
        random.choice(turtleList).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global gameOver
    countdownTurtle.penup() #We do not want a line to be drawn.
    countdownTurtle.hideturtle()#We do not want to see the image icon.
    countdownTurtle.color("black")

    top_width = screen.window_width() / 2
    top_height = screen.window_height() / 2
    #We take half of the total length since we start from the center of the screen.


    y = top_height * 0.8
    x = top_width * 0.8
    countdownTurtle.setposition(x, y)

    if time > 0:
        countdownTurtle.clear()
        countdownTurtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time -1), 1000)
    else:
        gameOver = True
        countdownTurtle.clear()
        hide_turtles()
        countdownTurtle.write(arg="Game Over!", move=False, align="center", font=FONT)

def start_game():
    turtle.tracer(0)
    setup_turtles()
    setup_score_turtle(),
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)

start_game()
turtle.mainloop()