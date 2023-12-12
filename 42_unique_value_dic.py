a = [{"a": "101"}, {"b": "102"}, {"c": "101"}, {
    "d": "103"}, {"e": "102"}, {"f": "103"}, {"g": "105"}]

unique_value = set(value for dic in a for value in dic.values())

print(unique_value)
