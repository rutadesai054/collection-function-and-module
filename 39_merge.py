def merge_two_dic(dic1, dic2):
    merged_dic = {**dic1, **dic2}
    return merged_dic


dic_a = {'a': 1, 'b': 2}
dic_b = {'b': 3, 'c': 4}

a = merge_two_dic(dic_a, dic_b)
print("merged dictinary is : ", a)
