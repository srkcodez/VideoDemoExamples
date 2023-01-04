from itertools import combinations
from matplotlib import pyplot as plt

# data input

list1 = [1, 3, 5, 7, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# list for all the combinations
list2 = []

# list for mean of all combinations
list3 = []

n = int(input("Enter the number of combinations you want: "))
comb_dict={}
if n > len(list1):
    print("Not enough numbers to make", n, "combinations")
else:

    for k in range(n):
        list2=[]
        list3=[]
        comb = combinations(list1, k)
        for i in list(comb):
            list2.append(i)
        #print("The combinations are:", list2)
        for n in list2:
            c = sum(n) / 2
            list3.append(c)
        #print("The mean of each combinations is:", list3)
        #plt.hist(list3, 10)
        comb_dict[k]=list3
        #plt.show()
for i in comb_dict.keys():
    print(comb_dict[i])

n=len(comb_dict.keys())

for i in range(n):
    plt.subplot(1,n,i+1)
    plt.hist(comb_dict[i])
plt.show()