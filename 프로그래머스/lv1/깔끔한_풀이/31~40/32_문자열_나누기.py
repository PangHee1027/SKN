def solution(s):
    answer = 0
    target_char = ""
    target = 0
    other = 0

    for c in s:
        # 기준 문자가 정해지지 않은 경우(새 분해 시작)
        if target == 0:
            target_char = c

        if c == target_char:
            target += 1
        else:
            other += 1

        # 두 글자 수가 같아지면 문자열 분리
        if target == other:
            answer += 1
            target = 0
            other = 0

    # 반복문이 끝나고 분리되지 않은 잔여 문자열이 남아있다면 +1
    if target > 0:
        answer += 1

    return answer