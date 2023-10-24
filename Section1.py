# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""

# def merge_lists(list1= [1, 2, 3, 4] , list2= [5, 6, 7, 8]):
def merge_lists(list1, list2):
    return list1 + list2
# result = merge_lists(list1=[1, 2, 3, 4], list2=[5, 6, 7, 8])
# result = merge_lists()
result = merge_lists(list1=["a", "b", "c", "d"], list2=[5, 6, 7, 8])
print(result)

# Assignment 2:
"""
    create a function called separate() that accepts a string as an argument
    and returns a list containing each of the characters of
    the string separated as individual items in the list.

    Make sure to test the function.
"""

def separate(string):
    return list(string)

test = separate('abcd')
print(test)
print(separate("hello there"))
# function can directly be used in print


# Assignment 3:
"""
Create a function called multi_merge that takes a list and a string
as arguments.

The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.

"""
def multi_merge(lists , string):
# return lists + list(string) + [string]
# x = multi_merge([1, 2, 3, 4], "abcd")
# print(x)
    return lists + list(string) + string.split()
# print(multi_merge([1, 2, 3, 4],"i m harshit"))
x = multi_merge([1, 2, 3, 4], "i am harshit")
print(x)
# split is a keyword used to separate words in a string


# Assignment 4:

"""
Define a function called last_list that can accept an unlimited number
of lists but returns only the last list.

Example:

    For example, the below function call should return ['mike', 'john']

    last_list([1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john'])

"""
def last_list(*args):
# return (args)
    return args[-1]
x = last_list([1, 2, 3, 4, 5], ['a', 'b', 'c'], ['mike', 'john'])
print(x)

def last_list1(*args):
    return args[-1:len(args)]
lists = last_list1([1, 2, 3, 4, 5], ['a', ' b', 'c'], [4, 5, 6, 7], ["aa", "bb", "cc", "dd"], ['mike', 'john'])
print(lists)


# Assignment 5:

"""
Define a function called key_list_items that can accept an unlimited number
of lists along with another argument. The function should return
the second_folder to last item in the specific list specified by the user of the function.

Example:

    For example, the below function call should return: jan

    key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])

"""

def key_list_items(key, **kwargs):
     value_list = kwargs[key]
     return value_list[-2]

# result = key_list_items("people", things=['book', 'tv', 'shoes'], people=['pete', 'mike', 'jan', 'tom'],
# ages=[20, 30, 40])
# result = key_list_items("ages", things=['book', 'tv', 'shoes'], people=['pete', 'mike', 'jan', 'tom'],
# ages=[20, 30, 40])
result = key_list_items("things", things=['book', 'tv', 'shoes'], people=['pete', 'mike', 'jan', 'tom'],
                 ages=[20, 30, 40])
print(result)