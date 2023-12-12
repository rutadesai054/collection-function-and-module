def remove_duplicate_list(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


original_list = [1, 5, 8, 8, 9, 6, 9, 6, 2, 3, 4]
real_list = remove_duplicate_list(original_list)

print("original list : ", original_list)
print("list after removing duplicates value :", real_list)
