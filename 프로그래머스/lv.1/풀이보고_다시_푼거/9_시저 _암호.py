def solution(s, n):
    answer = ''
    for i in s:
        if i:
            # 문자도 부등호가 먹는구나, 굳이 ord 로 아스키코드로 변환할 필요가 없네
            # 대문자인 경우
            if i >= 'A' and i <= 'Z':
                # 나머지 연산자 생각은 했는데 어떻게 쓸지 감이 안잡혔음
                # 정리하면 현재 문자 - 대문자 A 의 아스키 코드에 key 값을 더한 값을 26으로 나눔 -> 암호문 문자의 상대적 위치
                # + ord('A') -> 시작값에 상대적 위치를 더하여 문자를 구함
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            # 소문자인 경우
            elif i >= 'a' and i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            # 그 외의 경우
            # 문제에선 공백만 취급하니 공백을 넣었지만 answer += i 로 했으면 특수 문자들도 처리 가능
            else : answer += ' '
    return answer
