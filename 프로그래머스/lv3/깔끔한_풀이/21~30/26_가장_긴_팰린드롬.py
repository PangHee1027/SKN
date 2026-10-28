def solution(s):
    n = len(s)
    if n < 2:
        return n

    # 주어진 좌우 포인터에서 시작해 팰린드롬의 길이를 반환하는 함수
    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        # 멈춘 시점 직전까지가 팰린드롬이므로 길이는 (right - 1) - (left + 1) + 1
        return right - left - 1

    max_len = 1
    for i in range(n):
        # 1) 홀수 길이 팰린드롬 검사 (중앙이 i)
        max_len = max(max_len, expand(i, i))
        # 2) 짝수 길이 팰린드롬 검사 (중앙이 i와 i+1 사이)
        max_len = max(max_len, expand(i, i + 1))

    return max_len