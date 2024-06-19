import re

# sets the pattern allowed
pattern = r'[(]?[+-]?([0-9]*[.])?[0-9]+[)]?'

while True:

    # gets the user's coordinates
    response = input("Enter a coordinate (e.g. 3,4 or (5,2)) ")

    # if the response matches the pattern it plays the code
    if re.match(pattern, response):

        # removes the brackets and white space
        response = re.sub(r'[()\s]', r'', response)

        # sets the x to the first num and y to second num after split
        x_str, y_str = response.split(',')

        # turns the response into a list
        response = list(response)

        first_x = float(x_str)
        first_y = float(y_str)
        print(f"First x: {first_x} and First y: {first_y}")
    else:
        print("Only enter floats")
