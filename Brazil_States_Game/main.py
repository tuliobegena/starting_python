from writer_turtle import NUMBER_OF_STATES
import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("Estados Brasileiros")
image = "blank-map-of-brazil.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("states_coordinates.csv")
initial_list = df.state.to_list()
corrected_list = []

while len(corrected_list) < NUMBER_OF_STATES:
    answer_state = screen.textinput(f"Adivinhe um estado {len(corrected_list)}/{NUMBER_OF_STATES}",prompt="Qual nome de mais um estado?").title()
    print(answer_state)
    for i in range(NUMBER_OF_STATES):
        if answer_state == df.state[i] and answer_state in initial_list:
            corrected_list.append(df.state[i])
            corrected_list = sorted(set(corrected_list))
            initial_list.remove(df.state[i])
            writer = turtle.Turtle()
            writer.hideturtle()
            writer.penup()
            writer.goto(df.x[i], df.y[i])
            writer.write(df.state[i], font=("Arial", 18, "bold"))


screen.exitonclick()