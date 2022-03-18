import turtle
import pandas
import unicodedata


def clear_string(string):
    clean_string = ''.join(ch for ch in unicodedata.normalize('NFKD', string) if not unicodedata.combining(ch))
    return clean_string


screen = turtle.Screen()
screen.title("Brazil States Game")
image = "brazil-states.gif"
screen.addshape(image)
screen.setup(1000, 1000)
turtle.shape(image)

data = pandas.read_csv("27_states.csv")
all_states = data.state.to_list()
print(all_states)


guessed_states = []
while len(guessed_states) < 27:
    guess = screen.textinput(title=f"{len(guessed_states)}/27 States Correct", prompt="What's another state?").title()
    answer_state = clear_string(guess)
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
turtle.mainloop()



