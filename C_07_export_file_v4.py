import math
import pandas
from datetime import date


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

        # prints everything if the user chose to do so
        elif response == "all":
            print(answers[response])

            # returns in the same format in order to be written to txt file
            return answers[response]

        # prints the answer the user wanted
        elif response in allowed_responses:
            print(answers[response])

            return answers[response]

        else:
            print(f"Please enter a response in {allowed_responses}")


# sets up to_write list
to_write = []

# sets up the lists for panda dataframes
questions_list = ["Question 1: "]
equations_list = ["Equation 1"]
midpoints_list = ["Midpoint 1"]
distances_list = ["Distance 1"]
gradients_list = ["Gradient 1"]

# gets the 2 x and y points
first_x = 19
first_y = 5
second_x = 25
second_y = 21

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
all_answers = f"{equation}\n{midpoint}\n{distance}\n{gradient}\n"

# sets up a list of valid answers
valid_responses = ["gradient", "midpoint", "distance", "equation", "all"]

# sets up dict for pandas table
answers = {
    "Question": questions_list,
    "Equation": equations_list,
    "Midpoint": midpoints_list,
    "Distance": distances_list,
    "Gradient": gradients_list,
}

# puts the answers and questions into the dataframe
pandas_frame = pandas.DataFrame(answers)

pandas_frame = pandas_frame.set_index('Question')
print()
print(pandas_frame)

# change frame to a string so that we can export it to file
pandas_frame = pandas.DataFrame.to_string(pandas_frame)

# onto a txt file
to_write.append(pandas_frame)

# get current date for heading and filename
# get today's date
today = date.today()

# get day, month and year as individual string
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# write to file
# create file to hold data(add .txt extension)
file_name = input()
write_to = f"{file_name}.txt"

text_file = open(write_to, "w+")

heading = f"Coordinate Geometry Calculator Answers {day}/{month}/{year}"

# heading
text_file.write(f"***** {heading}"
                f" ***** \n \n")

# writes all the items into the text file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# closes file
text_file.close()
