def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str


tuple = ('r', 'u', 't', 'a')
str = convertTuple(tuple)
print(str)
