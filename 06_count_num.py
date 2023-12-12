def string_count(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1

    return count


string_list = ["level", "python", "noon", "hello", "wow"]
result = string_count(string_list)

print("List of strings:", string_list)
print("Number of strings with same first and last character:", result)
