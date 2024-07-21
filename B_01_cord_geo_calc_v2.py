import math
import pandas
import re
import random
from datetime import date


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
the second one (we ask you for both at the same time). 


The list of answers that we can calculate for you are: 
equation, gradient, midpoint and distance.

After we give you your answer we also put it all onto a txt file 
for you to view or share with others if you'd like to do so.

That's about it, thanks for using my coordinate geometry calculator! 

Note: Large numbers may affect how the table of answers is shown 
in the terminal but you will still see the full table if you 
look at the txt file.

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

        return round(gradient, 2)

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

    return x_mid, y_mid


# calculates the distance of the 2 points
def calc_distance(x1, y1, x2, y2):
    # calculates the distance between the two points
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return round(distance, 2)


# formats a number to an int
def format_int(num):
    # sets up a variable to compare the num to
    int_form_num = int(num)
    int(num)

    # compares the two, if they are the same it returns
    # the number as an integer
    if int_form_num == num:
        return int_form_num

    # else it returns the num as it is
    else:
        return num


# sets up to_write list
to_write = []

# sets up the variables for the coordinates
first_x = 0
first_y = 0
second_x = 0
second_y = 0

# sets up the lists for panda dataframes
questions_list = []
equations_list = []
midpoints_list = []
distances_list = []
gradients_list = []

# displays instructions if the user types "y" or "yes"
want_instructions = yes_no("Do you want to see the instructions?")

# if the user said yes it prints the instructions
if want_instructions == "yes":
    instructions()


# asks the user if they want a custom file name
custom_file = yes_no("Do you want a custom file name? If not we will use our default name. ")

# gets them to enter it if yes else it defaults it to something else
if custom_file == "yes":
    file_name = input("What name would you like? ")

else:

    number = random.getrandbits(16)

    # randomizes the numbers so it won't overwrite any files
    file_name = f"Coordinate_Geometry_Answers" \
                f"_{number}"

# question num for pandas table and for how many program will answer
question_num = 1

# makes sure the user enters a number above 0
while True:
    questions_needed = num_check("How many question do you need answered? ")

    # sends the users back to the start of the loop if their number is <= 0
    if questions_needed <= 0:
        print("Please only enter numbers higher than 0")
        continue

    else:
        break

while question_num <= questions_needed:

    # initiates first_coordinate and sets it
    # to true so the user enters the first coordinate
    first_coordinate = True

    # prints the question they are on
    print()
    print(f"Question {question_num}: ")

    while True:

        # gets the user's coordinates
        response = input("Enter a single coordinate (e.g. 3,4 or (5,2)): ")

        # # checks for emergency exits
        # if response == "xxx" and question_num != 1:
        #     response = yes_no("\nAre you sure you want to exit?")
        #
        #     if response == "no":
        #         continue
        #
        #     else:
        #         break
        #
        # else:
        #     print("Please enter at least one pair of coordinates")

        # sets the pattern allowed
        pattern = r'\(?-?\d+(\.\d+)?,\s?-?\d+(\.\d+)?\)?'

        # if the response matches the pattern it plays the code
        if re.match(pattern, response):
            # removes the brackets and white space
            response = re.sub(r'[()\s]', r'', response)

            # sets the x to the first num and y to second num after split
            x_str, y_str = response.split(',')

            # if ValueError:
            #
            #     print("Please enter the coordinate in the format (3,4) or 3,4 with only one coordinate each time. "
            #           "Spaces don't matter.\n")
            #     continue

            # sets the second point to their variables
            if first_coordinate is False:
                # sets the numbers for the second point
                second_x = float(x_str)
                second_y = float(y_str)
                break

            # converts the two strings into floats and sets it to the first point
            first_x = float(x_str)
            first_y = float(y_str)

            # sets variable to false and allow the
            # user to enter their second coordinate
            first_coordinate = False

        else:
            print("Only enter floats or enter your numbers in the format (3,4) or 3,4")

    # calculates the gradient
    gradient = calc_gradient(first_x, first_y, second_x, second_y)

    # if there is an error with the calculation fo the gradient
    # sends the user back to the start of the loop to re-enter their points
    if gradient == "yes":
        continue

    # finds the equation for between the two points
    y_intercept = first_y - gradient * first_x

    x_middle, y_middle = calc_midpoint(first_x, first_y, second_x, second_y)
    distance = calc_distance(first_x, first_y, second_x, second_y)

    # makes every integer into an integer and keeps floats as floats
    # and sets the values to their respective variables
    gradient, y_intercept, x_middle, y_middle, distance = map(format_int,
                                                              (gradient, y_intercept, x_middle, y_middle, distance))

    # appends and calculates (for some) the answers for the current coordinates
    equations_list.append(f"y = {gradient:.2f}x + {y_intercept:.2f}")
    midpoints_list.append(f"Midpoint: ({x_middle:.2f}, {y_middle:.2f})")
    distances_list.append(distance)
    gradients_list.append(gradient)

    # appends the coordinates for this question
    questions_list.append(f"Question {question_num}:")

    # updates the question counter
    question_num += 1

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

# write to file
# create file to hold data(add .txt extension)
write_to = f"{file_name}.txt"

text_file = open(write_to, "w+")

# get current date for heading and filename
# get today's date
today = date.today()

# get day, month and year as individual string
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

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

print("\nThanks for using my Calculator. "
      "All of these answers are also printed "
      f"onto a txt file called {write_to}.")
