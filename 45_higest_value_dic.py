from collections import Counter
a = {'A': 50, 'B': 83, 'C': 75, 'D': 58, 'E': 22, 'F': 67}
b = Counter(a)
highest_value = b.most_common(3)
print(a)
print("keys : values")
for i in highest_value:
    print(i[0], ":", i[1], " ")
