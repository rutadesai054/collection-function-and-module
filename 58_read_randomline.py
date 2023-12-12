import random


def random_line(file_name):
    line = open(file_name).read().splitlines()
    return random.choice(line)


print(random_line('43_zip_method.txt'))
