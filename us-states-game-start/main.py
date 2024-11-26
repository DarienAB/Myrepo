import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
guessed_states = []

turtle.shape(image)
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state's name? ").title()
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        data = pandas.DataFrame(missing_states)
        data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] #Since state is in the row with x and y we can use x's and y's column
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(state_data.state.item())



