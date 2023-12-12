def common_number(list1, list2):
    a1 = set(list1)
    b1 = set(list2)
    return bool(a1.intersection(b1))


list_1 = [11, 12, 13, 14, 15]
list_2 = [15, 16, 17, 18, 19]

if common_number(list_1, list_2):
    print("the list have at least one common number")
else:
    print("he list do not have any common number")
