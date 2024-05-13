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
    midpoint = f"Midpoint: ({x_mid:.2f}, {y_mid:.2f})"

    return midpoint


# calculates the distance of the 2 points
def calc_distance(x1, y1, x2, y2):
    # calculates the distance between the two points
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance


# checks that users enter a valid response
def print_answer(question, allowed_responses, answers, exit_code=None):

    while True:

        response = input(question).lower()

        # exits the loop
        if response == exit_code:
            break

        # prints the answer the user wanted
        elif response in allowed_responses:
            print(answers[response])

        # prints everything if the user chose to do so
        elif response == "all":

            for response in answers:
                print(answers[response])

        else:
            print(f"Please enter a response in {allowed_responses}")


# gets the 2 x and y points
first_x = num_check("What is your first x point?")
first_y = num_check("What is your first y point?")
second_x = num_check("What is your second x point?")
second_y = num_check("What is your second y point?")

# does all the calculations using the functions
gradient = calc_gradient(first_x, first_y, second_x, second_y)
midpoint = calc_midpoint(first_x, first_y, second_x, second_y)
distance = calc_distance(first_x, first_y, second_x, second_y)

# finds the equation for between the two points
y_intercept = first_y - gradient * first_x

# formats the answers properly for printing
equation = f"Equation: y = {gradient:.2f}x + {y_intercept:.2f}"
gradient = f"Gradient: {gradient:.2f} "
distance = f"Distance: {distance:.2f} "

# sets up a list of valid answers
valid_responses = ["gradient", "midpoint", "distance", "equation", "all"]

# sets up dict
answers = {
    "equation": equation,
    "midpoint": midpoint,
    "distance": distance,
    "gradient": gradient,
}

# asks the user what answers they'd like and prints them
print_answer("What answers would you like (<enter> to stop)?", valid_responses, answers, exit_code="")
