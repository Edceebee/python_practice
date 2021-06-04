# function that converts a list to a tuple

def convert(list1, list2):
    # list1 = []
    # list2 = []

    list3 = dict(zip(list1, list2))
    print(list3)
    # return list3


convert([1, 2, 3], ['one', 'two', 'three'])
