import pandas as pd
import turtle as t

tim = t.Turtle()

tim.hideturtle()
tim.penup()
screen = t.Screen()

screen.title('Guess The States !')
screen.setup(width=700, height=500)
image = './blank_states_img.gif'
screen.addshape(image)
t.shape(image)
data = pd.read_csv('./50_states.csv')
state_list = data.state.to_list()


guessed_states = []


while len(guessed_states) < 50:
    ans_state = screen.textinput(
        title=f'{len(guessed_states)}/50 States Correct', prompt='Please Enter Your Guess : ').title()
    if ans_state == 'Exit':
        missing_states = [
            state for state in state_list if state not in guessed_states]
        study_states = pd.DataFrame(missing_states)
        study_states.to_csv('./states_to_learn.csv')
        break
    elif ans_state in state_list:
        if ans_state not in guessed_states:
            guessed_states.append(ans_state)
            state_row = data[data['state'] == ans_state]

            tim.goto(int(state_row.x), int(state_row.y))
            tim.write(state_row.state.item(), align='center',
                      font=('Courier', 6, 'bold'))
