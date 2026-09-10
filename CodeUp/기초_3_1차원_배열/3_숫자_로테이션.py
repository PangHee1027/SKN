input()
list = list(map(int, input().split()))
start = 0
last = len(list)

for i in range(len(list)) :
    for j in range(start, last) :
        print(list[j], end = " ")
    list.append(list[i])
    start += 1
    last += 1
    print()
