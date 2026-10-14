import sys

sys.setrecursionlimit(20000)

def solution(storage, requests):
    h = len(storage)
    w = len(storage[0])
    storage = [list(x) for x in storage]
    dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def fork_lift(i, j, v) :
        possible = []
        if i == 0 or i == h - 1 or j == 0 or j == w - 1 :
            return True
        for dx, dy in dr :
            nx, ny = i + dx, j + dy
            if not storage[nx][ny] :
                if (nx, ny) not in v :
                    v.add((nx, ny))
                    possible.append(fork_lift(nx, ny, v))
        if any(possible) :
            return True

    for request in requests :
        crain = False
        possible = []
        if len(request) == 2 :
            request = request[0]
            crain = True
        for i in range(h) :
            for j in range(w) :
                if storage[i][j] == request :
                    if crain or fork_lift(i, j, {(i, j)}) :
                        possible.append((i, j))
    
        for x, y in possible :
            storage[x][y] = 0

        remain = 0

        for i in range(h) :
            for j in range(w) :
                if storage[i][j] :
                    remain += 1

    return remain

print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))
print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"]))