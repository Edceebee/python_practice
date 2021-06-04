# Given a Python list, remove all occurrence of 20 from the list

list1 = [5, 20, 15, 20, 25, 50, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, ]

for number in list1:
    if number == 20:
        list1.remove(20)
print(list1)

# list1 = [5, 20, 15, 20, 25, 50, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, ]
#
#
# def removeValue(sampleList, val):
#     return [value for value in sampleList if value != val]
#
#
# resList = removeValue(list1, 20)
# print(resList)
