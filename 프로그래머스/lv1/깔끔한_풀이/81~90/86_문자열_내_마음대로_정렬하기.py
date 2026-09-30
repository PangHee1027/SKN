def solution(strings, n):
    strings.sort()                   # 1. 사전순으로 먼저 정렬
    return sorted(strings, key=lambda x: x[n])  # 2. n번째 문자로 정렬