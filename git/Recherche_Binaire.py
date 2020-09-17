position = -1


def search(list, n):
    min = 0
    max = len(list) - 1


    while min <= max:
        milieu = (min + max) // 2

        if list[milieu] == n:
            globals()['position'] = milieu
            return True
        else:
            if list[milieu] < n:
                min = milieu + 1
            else:
                max = milieu - 1
    return False


list = [4, 7, 8, 12, 45, 99]

n = 99

if search(list, n):
    print("Found at position: ", position)
else:
    print("Not found.")