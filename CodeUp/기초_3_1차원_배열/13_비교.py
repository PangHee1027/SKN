n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    print(f"{i+1}:", end="")
    for j in range(n):
        if i == j:
            continue
        if arr[i] < arr[j]:
            print(" <", end="")
        elif arr[i] > arr[j]:
            print(" >", end="")
        else:
            print(" =", end="")
    print()
    