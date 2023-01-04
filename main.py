def LinearSearch(arr, pivot):
    for i in range(len(arr)):
        if pivot == arr[i]:
            return i
    return -1


res = LinearSearch([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 80)

if res == -1:
    print('element not found')
else:
    print('element found at %d' % (res + 1))
