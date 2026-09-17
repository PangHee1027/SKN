def solution(s):
    last_char = {}
    answer = []

    for i, char in enumerate(s):
        if char in last_char:
            answer.append(i - last_char[char])
        else:
            answer.append(-1)
            
        # 현재 문자의 최근 위치 업데이트 (공통 수행)
        last_char[char] = i

    return answer