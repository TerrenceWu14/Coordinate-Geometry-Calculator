# fixed answers
equation = "Equation: y = 5x + 2"
midpoint = "Midpoint: (22.3, 5)"
gradient = "Gradient: 5 "
distance = "Distance: 3.4"

# write to file
# create file to hold data(add .txt extension)
file_name = "Coordinate Geometry Calculator Answers.txt"
text_file = open(file_name, "w+")

to_write = [equation, midpoint, gradient, distance]

# heading
text_file.write(f"***** {file_name}"
                f"***** \n \n")

# heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# closes file
text_file.close()
