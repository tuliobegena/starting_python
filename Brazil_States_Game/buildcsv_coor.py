import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Estados Brasileiros")
image = "blank-map-of-brazil.gif"
screen.addshape(image)
turtle.shape(image)
NUMBER_OF_STATES = 26

with open("states.txt") as input:
    states_list = input.readlines()
for i, state in enumerate(states_list):
    states_list[i] = state.strip("\n")

counter = 0

def get_mouse_click_coor(x, y):
    print(x, y)
    global counter
    with open("states_coordinates.txt", "a") as output:
        text = f"{states_list[counter]},{x},{y}\n"
        output.write(text)
    counter += 1


while counter < NUMBER_OF_STATES:
    turtle.onclick(get_mouse_click_coor)

df = pd.read_csv("states_coordinates.txt", encoding="latin-1")
print(df)
df.to_csv("states_coordinates.csv", index=None)