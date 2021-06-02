# Write a Python program to sum all the items in a list.

def addNumbers(numbers, result=0):

    # result = 1

    for elements in numbers:
        result += elements
    return result


print(addNumbers([1, 2, 3, 4, 5]))
