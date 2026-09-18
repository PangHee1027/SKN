def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        # 제곱근이 정수이면(완전제곱수이면) 약수의 개수는 홀수
        if int(i**0.5) ** 2 == i:
            answer -= i
        else:
            answer += i
    return answer