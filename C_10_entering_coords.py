import re

# sets the pattern allowed
pattern = r'[+-]?([0-9]*[.])?[0-9]+'

while True:
    response = input()

    response = re.sub(r'[(),]', r'', response)
    print(response)

    response = list(response)
    print(response)

    first_x = response[0]
    first_y = response[1]

    print(f"First x: {first_x} and First y: {first_y}")

    #
    # if re.match(pattern, response):
    #     float(response)
    #     print(response)
    #
    # else:
    #     print("Only enter floats")
    #     continue
