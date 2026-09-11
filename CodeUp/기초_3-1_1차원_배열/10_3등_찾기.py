n = int(input())
friends = {}

for i in range(n) :
    a, b = map(str, input().split())
    friends[int(b)] = a

sorted = list(friends.keys())
sorted.sort()

print(friends[sorted[-3]])
