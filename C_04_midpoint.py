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


# calculates the midpoint of the 2 points
def calc_midpoint(x1, y1, x2, y2):

    # finds the x and y coordinates for the midpoints
    x_mid = (x2 + x1) / 2
    y_mid = (y2 + y1) / 2

    # puts the x and y middle points into one message
    # so that it displays as a coordinate
    midpoint = f"{x_mid}, {y_mid}"

    return midpoint


# gets the 2 x and y points
first_x = num_check("What is your first x point?")
first_y = num_check("What is your first y point?")
second_x = num_check("What is your second x point?")
second_y = num_check("What is your second y point?")

midpoint = calc_midpoint(first_x, first_y, second_x, second_y)

print(midpoint)
