while True:
    error = "Please only enter integers"

    try:
        number = float(input("Number: "))

    except ValueError:
        print(error)
