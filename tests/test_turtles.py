from random import randint
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=800, height=600)
user_input = screen.textinput("Turtle race bet", "Which turtle will win this race? Make your bet: ")


def create_turtles(height, colors):
    race_turtles = []
    num_turtle = len(colors)
    number = - (height // num_turtle)

    for num in range(num_turtle):
        temp = Turtle('turtle')
        temp.color(colors[num])
        temp.penup()
        temp.setposition(-340, number)
        number += 50
        race_turtles.append(temp)

    return race_turtles


colors = ['blue', 'red', 'pink', 'yellow', 'orange', 'black', 'green', 'violet', 'brown', 'grey']
turtles = create_turtles(700, colors)

countdown = Turtle()
countdown.hideturtle()
countdown.penup()
countdown.setposition(-50, 200)
for i in ["Ready...", "Set...", "Go!"]:
    countdown.clear()
    countdown.write(i, align="center", font=("Arial", 24, "bold"))
    time.sleep(1)

winner = None
game = True
while game:
    for race_turtle in turtles:
        distance = randint(2, 10)
        race_turtle.forward(distance)
        if race_turtle.xcor() > 300:
            game = False
            winner = race_turtle
            break

# winner
win_turtle = Turtle()
win_turtle.hideturtle()
win_turtle.penup()
win_turtle.setposition(-50, 250)
win_turtle.write(f"The winner is {winner.color()[0]}!", align="center", font=("Arial", 24, "bold"))

# celebrated
for _ in range(36):
    winner.right(10)
    time.sleep(0.05)

#bet
if user_input and user_input.lower() == winner.color()[0]:
    win_turtle.setposition(-50, 200)
    win_turtle.write("You are the winner!!!", align="center", font=("Arial", 24, "bold"))


time.sleep(3)
screen.bye()
