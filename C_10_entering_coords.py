import re

pattern = r'[+-]?([0-9]*[.])?[0-9]+'

while True:
    response = input()

    response = re.sub(r'[(),]', r'', response)
    print(response)

    response = re.split(r'', response)

    print(response)

    #
    # if re.match(pattern, response):
    #     float(response)
    #     print(response)
    #
    # else:
    #     print("Only enter floats")
    #     continue
