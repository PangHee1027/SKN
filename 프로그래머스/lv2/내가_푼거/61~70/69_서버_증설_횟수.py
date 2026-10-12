from collections import deque

def solution(players, m, k):
    answer = 0
    server = deque([0 for _ in range(k)], maxlen=k)

    for i, player in enumerate(players) :
        server.popleft()
        require = 0
        while player >= m * (sum(server) + require) + m :
            require +=1
        answer += require
        server.append(require)
    return answer

print(solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))
#print(solution([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], 5, 1))
#print(solution([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1))