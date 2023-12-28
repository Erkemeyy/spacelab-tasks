def pythagorean_triangle(sides):
    hypotenuse = max(sides)**2
    sum_of_squares_legs = 0
    # Calculate sum of squares on the legs
    for side in sides:
        if side != max(sides):
            sum_of_squares_legs += side ** 2
    # Check equality square of hypotenuse and square sum of legs
    if sum_of_squares_legs == hypotenuse:
        return True
    else:
        return False


print(pythagorean_triangle([5, 3, 4]))
