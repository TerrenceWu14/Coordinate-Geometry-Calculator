import random

number = random.getrandbits(16)

# randomizes the letters so it won't overwrite any files
file_name = f"Coordinate_Geometry_Answers" \
            f"_{number}"

print(file_name)
