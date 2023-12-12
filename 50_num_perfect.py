def perfect_number(number):
    sum = 0
    for i in range(1, number):
        if i % number == 0:
            sum += i
    return sum == number


print(perfect_number(6))
