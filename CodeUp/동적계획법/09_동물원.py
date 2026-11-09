n = int(input())

zoo = [[0] * (3) for _ in range(n)]
zoo[0] = [1, 1, 1]

for i in range(1, n) :
    zoo[i][0] = (zoo[i - 1][1] + zoo[i - 1][2]) % 9901
    zoo[i][1] = (zoo[i - 1][0] + zoo[i - 1][2]) % 9901
    zoo[i][2] = (zoo[i - 1][0] + zoo[i - 1][1] + zoo[i - 1][2]) % 9901

print(sum(zoo[-1]) % 9901)