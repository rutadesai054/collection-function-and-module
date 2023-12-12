def element_exist(tuple, element):
    return element in tuple


mytuple = (1, 2, 5, 6, 8, 9)
element_check = 5
a = element_exist(tuple, mytuple)
print("Tuple:", mytuple)
print(f"Element {element_check} exists: {a}")
