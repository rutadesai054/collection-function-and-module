def a(num):
    large_num = max(num)
    small_num = min(num)
    sum_avg_num = sum(num)
    return large_num, small_num, sum_avg_num


b = [5, 8, 9, 10, 23, 56, 7, 41]
large_num, small_num, sum_avg_num = a(b)
print("largest number is : ", large_num)
print("Smallest number is : ", small_num)
print("sum of number is : ", sum_avg_num)
