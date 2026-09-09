list1 = input().split()

for i in range(len(list1)) :
    list1[i] = int(list1[i])

list1.sort()

for i in list1 :
    print(int(i), end = " ")
