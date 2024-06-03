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

    # finds the actual gradient
    gradient = diff_in_y / diff_in_x

    return gradient


# calculates the midpoint of the 2 points
def calc_midpoint(x1, y1, x2, y2):
    # finds the x and y coordinates for the midpoints
    x_mid = (x2 + x1) / 2
    y_mid = (y2 + y1) / 2

    # puts the x and y middle points into one message
    # so that it displays as a coordinate
    midpoint = f"({x_mid:.2f}, {y_mid:.2f})"

    return midpoint


# calculates the distance of the 2 points
def calc_distance(x1, y1, x2, y2):
    # calculates the distance between the two points
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return round(distance, 2)


coordinates = []
equation = []
midpoint = []
distance = []
gradient = []

for item in range(0, 2):
    # gets the 2 x and y points
    first_x = num_check("What is your first x point?")
    first_y = num_check("What is your first y point?")
    second_x = num_check("What is your second x point?")
    second_y = num_check("What is your second y point?")

    coordinates.append(f"({first_x}, {first_y}), ({second_x}, {second_y})")

    # does all the calculations using the functions
    gradient = calc_gradient(first_x, first_y, second_x, second_y)
    midpoint = calc_midpoint(first_x, first_y, second_x, second_y)
    distance = calc_distance(first_x, first_y, second_x, second_y)

    # finds the equation for between the two points
    y_intercept = first_y - gradient * first_x

    equation.append(f"y = {gradient:.2f}x + {y_intercept:.2f}")
    midpoint.append(midpoint)
    distance.append(distance)
    gradient.append(gradient)

# sets up dict
answers = {
    "Coordinate": coordinates,
    "Equation": [equation],
    "Midpoint": [midpoint],
    "Distance": [distance],
    "Gradient": [gradient],
}

# sets up a list of valid answers
valid_responses = ["gradient", "midpoint", "distance", "equation", "a", "all", "g", "m", "d", "e"]

pandas_frame = pandas.DataFrame(answers)
pandas_frame = pandas_frame.set_index('Coordinate')

print(pandas_frame)
