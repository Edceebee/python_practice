pictures = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]

]

for items in pictures:
    for stuffs in items:
        if stuffs == 1:
            stuffs = '*'
        else:
            stuffs = ' '

        print(stuffs, end='')
    print()
