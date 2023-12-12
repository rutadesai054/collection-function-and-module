def second_smallest(numbers):

    if len(numbers) < 2:
        return "List should have at least two elements."

    smallest = second_smallest = float('inf')

    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_smallest


my_numbers = [5, 2, 8, 1, 7, 3]
result = second_smallest(my_numbers)

print("Original list:", my_numbers)
print("Second smallest number:", result)
