from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which color win race?"
                                                          "Enter color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
move_y = -90
all_turtle = []
for tims in color:
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(tims)
    tim.goto(x=-230, y=move_y)
    move_y += 30
    all_turtle.append(tim)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 220:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You have win, Winner color{winner}")
            else:
                print(f"Winner color {winner},You lose")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
