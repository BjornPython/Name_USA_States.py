import pandas
from turtle import Turtle

states_file = pandas.read_csv("50_states.csv")  # Reads the file using pandas
all_states = states_file.state.to_list()  # Gets all the states in the "50_states.csv" file and puts them in a list
guessed = []  # A list where all the user's correct answers are appended to.


def can_go():
    """Used in the while loop to check if
    you have guessed all the states."""
    if len(guessed) < 50:
        return True
    return False


def make_turtle(ans):
    """Makes a turtle to be used on
     top of the guessed state."""
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.ht()
    new_turtle.goto(find_state(ans))
    new_turtle.write(ans)
    return new_turtle


def check_state(answer):
    """Checks the user's input if it is
    a state in the USA."""
    answer = answer.title()
    if answer == "Exit":
        missing_states()
    if answer in all_states:
        make_turtle(answer)
        guessed.append(answer)


def missing_states():
    """Used to create a new .csv file with all
    the states not answered by the user."""
    miss_states = []
    for state in all_states:
        if state not in guessed:
            miss_states.append(state)
    missing = pandas.DataFrame(miss_states)
    missing.to_csv("States_to_Learn.csv")


def find_state(answer):
    """Used to find the state's x and y coordinates in the picture."""
    state_data = states_file[states_file.state == answer]
    x = int(state_data["x"])
    y = int(state_data["y"])
    print(x)
    print(y)
    return x, y


def break_loop(answer):
    """Used to break the while loop if the
    user's input is "Exit" """
    answer = answer.title()
    return answer == "Exit"  # Returns True if answer == "Exit"
