def multiple_key(dic, keys):
    return all(key in dic for key in keys)


a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

b = ['a', 'c', 'g']
c = multiple_key(a, b)
print(f"keys are exist : {c}")
