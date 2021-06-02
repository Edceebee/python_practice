# Write a Python program to get the largest number from a list.

def largestNumber(numbers):
    largest = 0

    for elements in numbers:
        if elements > largest:
            largest = elements

    return largest


print(largestNumber([1, 2, 3, 3, 4, 5, 5]))
