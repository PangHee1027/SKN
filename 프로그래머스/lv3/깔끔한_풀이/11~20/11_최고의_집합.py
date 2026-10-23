def solution(n, s):
    if n > s:
        return [-1]
    
    base = s // n       # 기본이 되는 몫
    rem = s % n         # 1씩 더 배분해야 하는 나머지 개수
    
    # 작은 값들과 (기본 몫 + 1)인 값들을 합치면 자연스럽게 오름차순이 됩니다.
    return [base] * (n - rem) + [base + 1] * rem