def format_int(num):
    int_form_num = int(num)
    int(num)

    if int_form_num == num:
        return int_form_num
    else:
        return num


gradient = 5.2
y_intercept = 10.0
midpoint = -2.64
distance = 3

gradient, y_intercept, midpoint, distance = map(format_int, (gradient, y_intercept, midpoint, distance))

print(gradient)
print(y_intercept)
print(midpoint)
print(distance)
