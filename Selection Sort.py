

def SelectionSort(array):
    for i in range(len(array)):
        minpos=i
        for j in range(i+1,len(array)):
            if array[minpos]>array[j]:
                minpos=j
        array[i],array[minpos]=array[minpos],array[i]
    return array


arr=SelectionSort([70,20,33,10])

for i in arr:
    print(i)