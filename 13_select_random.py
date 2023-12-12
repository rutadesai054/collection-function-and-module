import random


def select_random_item(my_list):
    random_item = random.choice(my_list)
    return random_item


mylist = [1, 4, 5, 8, 9, 6, 3, 2]
random_item = select_random_item(mylist)

print("Original list:", mylist)
print("Randomly selected item:", random_item)
