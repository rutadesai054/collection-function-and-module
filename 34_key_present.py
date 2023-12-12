a = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def key_present(x):
    if x in a:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')


key_present(5)
