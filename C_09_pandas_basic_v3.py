import pandas
import math


# checks that the input is a number

def num_check(question):
    while True:

        # sets up error message
        error = "Please only enter numbers"

        # tries to convert number to a float

        try:
            number = float(input(question))
            return number

        # if it can't convert the input into a float it then prints the error message and sends the user back to the
        # start of the loop
        except ValueError:
            print(error)


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
    midpoint = f"({x_mid:.2f}, {y_mid:.2f})"

    return midpoint


# calculates the distance of the 02 points
def calc_distance(x1, y1, x2, y2):
    # calculates the distance between the two points
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return round(distance, 2)


# sets up the lists for panda dataframes
questions_list = []
equations_list = []
midpoints_list = []
distances_list = []
gradients_list = []
question_num = 0

for item in range(0, 2):
    question_num += 1
    # gets the 2 x and y points
    first_x = num_check("What is your first x point?")
    first_y = num_check("What is your first y point?")
    second_x = num_check("What is your second x point?")
    second_y = num_check("What is your second y point?")

    # appends the coordinates for this question
    questions_list.append(f"Question {question_num}:")

    # calculates the gradient
    gradient = calc_gradient(first_x, first_y, second_x, second_y)

    # finds the equation for between the two points
    y_intercept = first_y - gradient * first_x

    # appends and calculates (for some) the answers for the current coordinates
    equations_list.append(f"y = {gradient:.2f}x + {y_intercept:.2f}")
    midpoints_list.append(calc_midpoint(first_x, first_y, second_x, second_y))
    distances_list.append(calc_distance(first_x, first_y, second_x, second_y))
    gradients_list.append(gradient)

# sets up dict
answers = {
    "Question": questions_list,
    "Equation": equations_list,
    "Midpoint": midpoints_list,
    "Distance": distances_list,
    "Gradient": gradients_list,
}

# sets up a list of valid answers
valid_responses = ["gradient", "midpoint", "distance", "equation", "a", "all", "g", "m", "d", "e"]

pandas_frame = pandas.DataFrame(answers)
pandas_frame = pandas_frame.set_index('Question')
print()
print(pandas_frame)
