def sort(list):
    for i in range(len(list)):
        minpos = i
        for j in range(i, len(list)):
            if list[j] < list[minpos]:
                minpos = j

        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp


list = [5, 3, 8, 6, 7, 2, 0]
sort(list)

print(list)
