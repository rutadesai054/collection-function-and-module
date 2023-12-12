def sum_divisors(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i) == 0:
            divisors.append(i)
    return sum(divisors)


print(sum_divisors(8))
print(sum_divisors(12))
