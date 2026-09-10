n, c = map(int, input().split())
student = list(map(int, input().split()))
student.sort()
count = 0

for i in student :
    print(i, end = " ")
    count += 1
    if count == c :
        print()
        count = 0
