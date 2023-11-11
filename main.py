import turtle, pandas


screen = turtle.Screen()
screen.title("U.S states game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_column = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    
    state_answer = screen.textinput(title=f"Guessed {len(guessed_states)}/50 correct states", prompt="What's another state in the USA:").title()

    if state_answer == "Exit":
        unknown_states = [states for states in states_column if states not in guessed_states]
        new_data = pandas.DataFrame(unknown_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if state_answer in states_column:
        guessed_states.append(state_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = data[data.state == state_answer]
        t.goto(int(state_row.x), int(state_row.y))
        t.write(state_row.state.item())

