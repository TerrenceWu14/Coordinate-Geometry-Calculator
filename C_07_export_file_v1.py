# fixed answers
equation = "Equation: y = 5x + 2"
midpoint = "Midpoint: (22.3, 5)"
gradient = "Gradient: 5 "
distance = "Distance: 3.4"

answers_file = f"{equation} \n{midpoint} \n{gradient} \n{distance} \n"

# write to file
# create file to hold data(add .txt extension)
file_name = "Coordinate Geometry Calculator Answers.txt"
text_file = open(file_name, "w+")

# heading
text_file.write(f"***** {file_name}"
                f"***** \n \n")

text_file.write(answers_file)

# closes file
text_file.close()

