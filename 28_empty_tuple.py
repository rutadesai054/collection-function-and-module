def remove_empty_tuple(tuple):
    non_empty_tuple = [tup for tup in tuple if tup]
    return non_empty_tuple


tuple = [(1, 2), (), (5, 6), ()]
a = remove_empty_tuple(tuple)
print("list with empty tuple is : ", tuple)
print("list without empty tuple is : ", a)
