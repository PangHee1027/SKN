def solution(strings, n):
    return sorted(strings, key = lambda x:(x[n], x))

print(solution(["cnbc", "anbcd"], 1))