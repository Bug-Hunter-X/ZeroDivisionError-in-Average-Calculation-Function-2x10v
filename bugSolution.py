def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    if all(num == 0 for num in numbers):
        return 0 # Handle all zero case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_zero_list = [0,0,0]
average_zero = calculate_average(my_zero_list)
print(f"The average of a zero list is: {average_zero}")
