def empty_list(mylist):
    return len(mylist) == 0


emptylist = []
non_emptylist = [1, 5, 6, 9]

print("empty list is ", empty_list(emptylist))
print("non empty list is ", empty_list(non_emptylist))
