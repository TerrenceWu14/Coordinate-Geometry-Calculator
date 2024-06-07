import math
import pandas


# checks that the user typed yes or no
def yes_no(question):
    while True:

        # asks the question
        response = input(question).lower()

        # sets up yes or no dict
        yes_or_no = {
            "y": "yes",
            "n": "no",
        }

        # checks if the first letter of the response
        # fits the keys in the dict
        if response[:1] in yes_or_no:
            return yes_or_no[response[:1]]

        # prints the error message
        else:
            print("Please enter yes or no\n")


# Displays instructions
def instructions():
    print('''

***** Instructions *****

To begin, you enter your first x and y coordinates along with
the second one. Then enter what answer's you'd like to see, for
example: "equation" and it will give you the equation according 
to the two x and y points you entered. 

The list of answers that we can calculate for you are: 
equation, gradient, midpoint and distance.

After we give you your answer we also put it all onto a txt file 
for you to view or share with others if you'd like to do so.

That's about it, thanks for using my coordinate geometry calculator! 

*****************************************************************
    ''')


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
    midpoint = f"Midpoint: ({x_mid:.2f}, {y_mid:.2f})"

    return midpoint


# calculates the distance of the 2 points
def calc_distance(x1, y1, x2, y2):
    # calculates the distance between the two points
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return round(distance, 2)


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


# sets up to_write list
to_write = []

# sets up the lists for panda dataframes
questions_list = []
equations_list = []
midpoints_list = []
distances_list = []
gradients_list = []

# displays instructions if the user types "y" or "yes"
want_instructions = yes_no("Do you want to see the instructions?")

if want_instructions == "yes":
    instructions()

# question num for pandas table and for how many program will answer
question_num = 0
questions_needed = num_check("How many question do you need answered? ")

while question_num < questions_needed:
    # gets the 2 x and y points
    first_x = num_check("What is your first x point?")
    first_y = num_check("What is your first y point?")
    second_x = num_check("What is your second x point?")
    second_y = num_check("What is your second y point?")

    # calculates the gradient
    gradient = calc_gradient(first_x, first_y, second_x, second_y)

    # if there is an error with the calculation fo the gradient
    # sends the user back to the start of the loop to re-enter their points
    if gradient == "yes":
        continue

    # finds the equation for between the two points
    y_intercept = first_y - gradient * first_x

    # appends and calculates (for some) the answers for the current coordinates
    equations_list.append(f"y = {gradient:.2f}x + {y_intercept:.2f}")
    midpoints_list.append(calc_midpoint(first_x, first_y, second_x, second_y))
    distances_list.append(calc_distance(first_x, first_y, second_x, second_y))
    gradients_list.append(gradient)

    question_num += 1

    # appends the coordinates for this question
    questions_list.append(f"Question {question_num}:")

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

# sets up dict
# answers = {
#     "e": equation,
#     "m": midpoint,
#     "d": distance,
#     "g": gradient,
#     "a": all_answers,
# }

# asks the user what answers they'd like and prints them
# print()
# wanted_answers = print_answer("What answers would you like?", valid_responses, answers)

# change frame to a string so that we can export it to file
pandas_frame = pandas.DataFrame.to_string(pandas_frame)

# onto a txt file
to_write.append(pandas_frame)

# write to file
# create file to hold data(add .txt extension)
file_name = "Coordinate Geometry Calculator Answers.txt"
text_file = open(file_name, "w+")

# heading
text_file.write(f"***** {file_name}"
                f" ***** \n \n")

# writes all the items into the text file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# closes file
text_file.close()
