# formats the equation according to the y int
def format_equation(gradient, y_int):

    # makes the + a - symbol instead if it's a negative
    if y_int < 0:
        equation = f"y = {gradient}x - {abs(y_int)}"

    else:
        equation = f"y = {gradient}x + {y_int}"

    return equation


while True:
    gradient = int(input("Gradient: "))
    y_int = int(input("Y int: "))

    print(format_equation(gradient, y_int))
