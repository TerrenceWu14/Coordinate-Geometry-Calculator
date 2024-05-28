import math
import pandas as pd


# calculates the gradient of the 2 points
def calc_gradient(x1, y1, x2, y2):
    # finds the difference in the 2 x and y points
    diff_in_y = y2 - y1
    diff_in_x = x2 - x1

    # tries to divide the two variables
    try:
        # finds the actual gradient
        gradient = diff_in_y / diff_in_x

        return gradient

    # prints error message if it is not able to be divided
    except ZeroDivisionError:
        print()
        print("Check if it's a horizontal or vertical line.\nThis is because "
              "the gradient is 0 or indefinite from our calculations.\n"
              "Otherwise please re-enter your x and y points.")
        print()

        re_enter = "yes"

        return re_enter


# calculates the midpoint of the 2 points
def calc_midpoint(x1, y1, x2, y2):
    # finds the x and y coordinates for the midpoints
    x_mid = (x2 + x1) / 2
    y_mid = (y2 + y1) / 2

    # puts the x and y middle points into one message
    # so that it displays as a coordinate
    midpoint = f"Midpoint: ({x_mid:.2f}, {y_mid:.2f})"

    return midpoint


# calculates the distance of the 2 points
def calc_distance(x1, y1, x2, y2):
    # calculates the distance between the two points
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance


# checks that users enter a valid response
def print_answer(question, allowed_responses, answers):
    while True:

        response = input(question).lower()

        # prints everything if the user chose to do so according to the first
        # letter of the response
        if response[:1] == "a":
            print()
            print(answers[response[:1]])

            # returns in the same format in order to be written to txt file
            return answers[response[:1]]

        # prints the answer the user wanted according
        # to the same format as the previous if statement
        elif response[:1] in allowed_responses:
            print()
            print(answers[response[:1]])

            return answers[response[:1]]

        else:
            print(f"Please enter a response in {allowed_responses}")


# gets the 2 x and y points
first_x = 2.5
first_y = 7
second_x = 7.5
second_y = 21

# calculates the gradient, midpoint and distance
gradient = calc_gradient(first_x, first_y, second_x, second_y)
midpoint = calc_midpoint(first_x, first_y, second_x, second_y)
distance = calc_distance(first_x, first_y, second_x, second_y)

# finds the equation for between the two points
y_intercept = first_y - gradient * first_x

# formats the answers properly for printing
equation = f"Equation: y = {gradient:.2f}x + {y_intercept:.2f}"
gradient = f"Gradient: {gradient:.2f} "
distance = f"Distance: {distance:.2f} "
all_answers = f"{equation}\n{midpoint}\n{distance}\n{gradient}\n"

# sets up dict
answers = {
    "e": equation,
    "m": midpoint,
    "d": distance,
    "g": gradient,
    "a": all_answers,
}

pandas_frame = pd.Series(answers, None)
total_won = pandas_frame.at["something", 'Total']

# set index at end (before printing)
pandas_frame = pandas_frame.set_index('Answers')
