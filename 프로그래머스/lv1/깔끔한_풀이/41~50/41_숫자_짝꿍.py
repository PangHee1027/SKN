def solution(X, Y):
    result = []

    # 9부터 0까지 내림차순으로 확인 (자동 정렬 효과)
    for i in range(9, -1, -1):
        char = str(i)
        cnt = min(X.count(char), Y.count(char))
        result.append(char * cnt)

    answer = "".join(result)

    # 1. 짝꿍이 존재하지 않는 경우
    if not answer:
        return "-1"

    # 2. 가장 큰 숫자가 '0'인 경우 (전체가 0인 경우)
    if answer[0] == "0":
        return "0"

    return answer