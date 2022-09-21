import turtle
from turtle import Screen
from get_state_info import *

screen = Screen()
background = "blank_states_img.gif"
screen.addshape(background)
turtle.shape(background)

while can_go():
    # Take answer from user
    user_answer = screen.textinput(title=f"{len(guessed)}/50 states guessed", prompt="what's another states name?")
    check_state(user_answer)  # Check the answer of user
    if break_loop(user_answer):  # Break loop if user's answer is "Exit"
        break

screen.mainloop()


