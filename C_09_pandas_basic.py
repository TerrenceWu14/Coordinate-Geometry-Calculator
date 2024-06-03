import pandas


coordinates = "(3, 5)"

# list to hold the answers
answer_1 = ["equation: 3x + 2"]
answer_2 = ["midpoint: 5,3"]
answer_3 = ["distance: 5"]

# sets up dict
answers = {
    "Coordinate": coordinates,
    "equation": answer_1,
    "midpoint": answer_2,
    "distance": answer_3,
}

# sets up a list of valid answers
valid_responses = ["gradient", "midpoint", "distance", "equation", "a", "all", "g", "m", "d", "e"]


pandas_frame = pandas.DataFrame(answers)
pandas_frame = pandas_frame.set_index('Coordinate')


print(pandas_frame)

