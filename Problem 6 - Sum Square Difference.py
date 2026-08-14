numbers = [x for x in range(1, 101)]
sum_of_squares = sum(x**2 for x in numbers)
sum_of_numbers_sq = sum(numbers)**2
print("The difference is:", sum_of_numbers_sq - sum_of_squares)

    