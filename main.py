import turtle
import pandas

screen = turtle.Screen()
image = "indian_states3.gif"
screen.setup(width=580, height=699)
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("states.csv")
states_list = data["state"]
# print(len(states_list))
correct = []
while len(correct) < 29:
    user_text = screen.textinput(title=f"{len(correct)}/29 States Guessed", prompt="What's another state?")
    if user_text.lower() == "exit":
        missing = []
        for state in states_list:
            if state not in correct:
                missing.append(state)
        # print(missing)
        break
    for i in range(0, len(states_list)):
        if states_list[i].lower() == user_text.lower():
            correct.append(states_list[i])
            name = turtle.Turtle()
            name.hideturtle()
            name.penup()
            row = data[data.state == states_list[i]]
            name.goto(x=int(row.x), y=int(row.y))
            name.write(states_list[i])

new_data = pandas.DataFrame(missing)
new_data.to_csv("missing_states.csv")
