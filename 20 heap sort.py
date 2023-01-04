
def heapsort(ele):

    #construct heap tree
    for j in range(len(ele ) - 2//2 ,-1 ,-1):
        siftdown(ele ,j ,len(ele))

    #perform heap sort
    for k in range(len(ele ) -1 ,0 ,-1):
        swap(ele ,0 ,k)
        siftdown(ele ,0 ,k)

def swap(ele ,i ,j):
    ele[i] ,ele[j ] =ele[j] ,ele[i]


def siftdown(ele ,i ,upr):

    while(True):

        l , r = i* 2 + 1, i * 2 + 2
        
        if max(l, r) < upr:
            if ele[i] >= max(ele[l], ele[r]):
                break
            elif ele[l] > ele[i]:
                swap(ele, l, i)
                i = l
            elif ele[r] > ele[i]:
                swap(ele, r, i)
                i = r
        elif l < upr:
            if ele[l] > ele[i]:
                swap(ele, i, l)
                i = l
            else:
                break
        elif r < upr:
            if ele[r] > ele[i]:
                swap(ele, i, r)
                i = r
        else:
            break


ele = [5, 16, 8, 14, 20, 1, 26]

heapsort(ele)

print(ele)
