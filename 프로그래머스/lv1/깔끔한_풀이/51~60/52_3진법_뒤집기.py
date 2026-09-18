def solution(n):
    result = ""
    # n을 3으로 나누며 나머지를 바로 뒤에 붙임 -> 이미 뒤집힌 3진법 완성
    while n > 0:
        result += str(n % 3)
        n //= 3

    # 3진법 문자열을 10진수로 변환
    return int(result, 3)