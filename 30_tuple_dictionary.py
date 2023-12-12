def convert(tuple, dictionary):
    for a, b in tuple:
        dictionary.setdefault(a, []).append(b)
        return dictionary


tuple = [("ruta", 24), ("om", 18), ("geeta", 45), ("sanjay", 50)]
dict = {}
a = convert(tuple, dict)
print(a)
