# Merging two Python dictionaries into one

def merge_dict(dict1, dict2):
    dict3 = {**dict1, **dict2}

    print(dict3)


merge_dict({1: 'one', 2: 'two'}, {3: 'three', 4: 'four'})
