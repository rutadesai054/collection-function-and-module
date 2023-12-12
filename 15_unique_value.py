def unique_value(input):
    u_v = list(set(input))
    return (u_v)


my_list = [1, 5, 8, 9, 6, 7, 4, 2, 5, 4, 8, 7]
a = unique_value(my_list)

print("original list is : ", my_list)
print("unique value is : ", a)
