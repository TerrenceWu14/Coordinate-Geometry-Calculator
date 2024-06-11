import re

pattern = r'[+-]?([0-9]*[.])?[0-9]+'

while True:
    response = input()

    if re.match(pattern, response):
        float(response)
        print(response)

    else:
        print("Only enter floats")
        continue
