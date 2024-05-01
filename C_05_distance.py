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


# calculates the distance of the 2 points
def calc_distance(x1, y1, x2, y2):

    # calculates the distance between the two points
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance


# gets the 2 x and y points
first_x = num_check("What is your first x point?")
first_y = num_check("What is your first y point?")
second_x = num_check("What is your second x point?")
second_y = num_check("What is your second y point?")

distance = calc_distance(first_x, first_y, second_x, second_y)

print(distance)
