test_list = [5, 8, 9, 6, 3, 8, 5, 2]
print("original list is : ", test_list)

sublist = [8, 9, 2]
print("sublist is :", sublist)
a = 0
res = False
for i in sublist:
    if i in sublist:
        a = a+1
if (a == len(sublist)):
    res = True

print("is sublist present in list ? :", res)
