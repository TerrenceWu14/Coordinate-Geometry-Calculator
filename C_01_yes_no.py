# checks that the user typed yes or no
def yes_no(question):
    while True:

        # asks the question
        response = input(question).lower()

        # sets up yes or no dict
        yes_or_no = {
            "y": "yes",
            "n": "no",
        }

        # checks if the first letter of the response
        # fits the keys in the dict
        if response[:1] in yes_or_no:
            return yes_or_no[response]

        # prints the error message
        else:
            print("Please enter yes or no\n")


# Main routine goes here
ok = yes_no("Yes or no? ")
print(ok)
