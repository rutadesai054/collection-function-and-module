from collections import Counter
a1 = {'a': 100, 'b': 200, 'c': 300}
b1 = {'a': 300, 'b': 200, 'd': 400}

c = Counter(a1)+Counter(b1)
print(c)
