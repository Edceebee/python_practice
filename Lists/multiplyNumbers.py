# Write a Python program to multiplies all the items in a list.

def multiplyNumbers(numbers):
    result = 1
    for elements in numbers:
        result *= elements

    return result


print(multiplyNumbers([1, 2, 4]))
