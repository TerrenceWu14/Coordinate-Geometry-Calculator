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

        # prints everything if the user chose to do so
        if response[:1] == "a":
            print(answers[response[:1]])

            # returns in the same format in order to be written to txt file
            return answers[response[:1]]

        # prints the answer the user wanted
        elif response[:1] in allowed_responses:
            print(answers[response[:1]])

            return answers[response[:1]]

        else:
            print(f"Please enter a response in {allowed_responses}")


# sets up to_write list
to_write = []

while True:

    # gets the 2 x and y points
    first_x = 13.6
    first_y = 14.3
    second_x = 20
    second_y = 15

    # calculates the gradient, midpoint and distance
    gradient = calc_gradient(first_x, first_y, second_x, second_y)
    midpoint = calc_midpoint(first_x, first_y, second_x, second_y)
    distance = calc_distance(first_x, first_y, second_x, second_y)

    # if there is an error with the calculation fo the gradient
    # sends the user back to the start of the loop to re-enter their points
    if gradient == "yes":
        continue

    else:
        break


# finds the equation for between the two points
y_intercept = first_y - gradient * first_x

# formats the answers properly for printing
equation = f"Equation: y = {gradient:.2f}x + {y_intercept:.2f}"
gradient = f"Gradient: {gradient:.2f} "
distance = f"Distance: {distance:.2f} "
all_answers = f"{equation}\n{midpoint}\n{distance}\n{gradient}\n"

# sets up a list of valid answers
valid_responses = ["gradient", "midpoint", "distance", "equation", "all", "g", "m", "d", "e"]

# sets up dict
answers = {
    "e": equation,
    "m": midpoint,
    "d": distance,
    "g": gradient,
    "a": all_answers,
}

# asks the user what answers they'd like and prints them
print()
wanted_answers = print_answer("What answers would you like?", valid_responses, answers)

# appends the wanted answers into a list to be written
# onto a txt file
to_write.append(wanted_answers)

# write to file
# create file to hold data(add .txt extension)
file_name = "Coordinate Geometry Calculator Answers.txt"
text_file = open(file_name, "w+")

# heading
text_file.write(f"***** {file_name}"
                f" ***** \n \n")

# heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# closes file
text_file.close()
