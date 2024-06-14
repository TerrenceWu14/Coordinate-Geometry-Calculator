import re

# sets the pattern allowed
pattern = r'[(]?[+-]?([0-9]*[.])?[0-9]+[)]?'

# gets the user's coordinates
response = input()

# if the response matches the pattern it plays the code
if re.match(pattern, response):

    # subs the brackets and commas with a whitespace
    response = re.sub(r'[(),]', r'', response)

    # turns the response into a list
    response = list(response)

    # sets the coordinate to their respective variables
    first_x = response[0]
    first_y = response[1]

    print(f"First x: {first_x} and First y: {first_y}")

else:
    print("Only enter floats")
