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


# gets the 2 x and y points
first_x = num_check("What is your first x point?")
first_y = num_check("What is your first y point?")
second_x = num_check("What is your second x point?")
second_y = num_check("What is your second y point?")

# calculates the gradient
gradient = calc_gradient(first_x, first_y, second_x, second_y)

y_intercept = first_y - gradient * first_x

equation = f"y = {gradient}x + {y_intercept}"

print(equation)
