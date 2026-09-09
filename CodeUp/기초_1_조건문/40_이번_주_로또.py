a = input().split()
b = input().split()
check = 0
result = [0, 0, 0, 5, 4, [3, 2], 1]

def bonus(num1, list1) :
    for i in range(len(list1)) :
        if num1 == list1[i] :
            return 1
    return 0

for i in(range(len(b))) :
    for j in(range(len(b))) :
        if a[i] == b[j] :
            check += 1

print(result[check] if check != 5 else result[5][bonus(a[6], b)])
