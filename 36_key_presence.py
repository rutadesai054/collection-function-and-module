# How Do You Check The Presence Of A Key In A Dictionary?
# To check the presence of a key in a dictionary in Python, you can use the in operator or the get() method. Here's how you can do it:

# Using the in operator:
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Check if a key is present
if 'a' in my_dict:
    print('Key "a" is present in the dictionary')
# This method is straightforward and commonly used.

# Using the get() method:
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Check if a key is present using get()
value = my_dict.get('a')

# if value is not None:
#     print('Key "a" is present in the dictionary')
# The get() method returns None if the key is not found. You can customize the default value returned by providing a second argument to get(), like my_dict.get('a', default_value).

# Using try-except block:

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Check if a key is present using try-except
try:
    value = my_dict['a']
    print('Key "a" is present in the dictionary')
except KeyError:
    print('Key "a" is not present in the dictionary')
# This method involves handling a potential KeyError using a try-except block.

# The first method ('a' in my_dict) is the most commonly used and is considered more Pythonic. Use the method that fits your coding style and specific requirements.
