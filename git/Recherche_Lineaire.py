position = -1


def search(list, n):
    i = 0

    while i < len(list):

        if list[i] == n:
            globals()['position'] = i
            return True
        i += 1
    return False


list = [4, 7, 8, 12, 45, 99]

n = 4

if search(list, n):
    print("Found at position: ", position)
else:
    print("Not found.")