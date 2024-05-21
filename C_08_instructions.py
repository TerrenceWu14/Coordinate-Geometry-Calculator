def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("you didn't choose a valid option (yes/no)")


# Displays instructions
def instructions():
    print('''

***** Instructions *****

To begin, you enter your first x and y coordinates along with
the second one. Then Enter what answer's you'd like to see, for
example: "equation" and it will give you the equation according 
to the two x and y points you entered. 

The list of answers that we can calculate for you are: 
equation, gradient, midpoint and distance.

After we give you your answer we also put it all onto a txt file 
for you to view or share with others if you'd like to do so.

That's about it, thanks for using my coordinate geometry calculator! 

*****************************************************************
    ''')


want_instructions = yes_no("Do you want to see the instructions?")

if want_instructions == "yes":
    instructions()
