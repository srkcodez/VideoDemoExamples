# logic for insertion sort
def linear_search(a, n, pivot):
    for i in range(n):
        if a[i]==pivot:
            return i
    return -1


a = []
n = int(input())
for i in range(0, n):
    a.append(int(input()))
pivot=int(input())
res=linear_search(a, n,pivot)
if res==-1:
    print("not found")
else:
    print("element is present at ",res+1,"position")