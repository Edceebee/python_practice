# someList = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# newList = []
#
# for items in someList:
#     if items not in newList:
#         newList.append(someList)
#     else:
#         print(items, end=' ')
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# my_list = sorted(some_list)

duplicates = []
for i in some_list:
    if some_list.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)
print(duplicates)
