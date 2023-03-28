# import csv
# with open("weather_data.csv")as data_files:
#     data=csv.reader(data_files)
#     temperature=[]
#     for row in data:
#         if row[1]!="temp":
#             temperature.append(int(row[1]))
#         print(row)
#     print(temperature)


# import pandas
# data=pandas.read_csv("weather_data.csv")
# print(data)
# data_dict=data.to_dict()
# print(data_dict)
#
# temp_list=data["temp"].to_list()
# print(temp_list)
#
# average=sum(temp_list)/len(temp_list)
# print(average)
#
# #or
# print(data["temp"].mean())
#
# print(data["temp"].max())


# new_data.to_csv("fur_color_Count.csv")

import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
print(data)
guessed_states = []
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="WHats another state's name").title()
    print(answer_state)

    if answer_state == "Exit":
        # missing_states = []
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = data[data["state"] == answer_state]
        t.goto(int(row["x"]), int(row["y"]))
        t.write(answer_state)

screen.exitonclick()
