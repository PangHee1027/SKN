from collections import Counter

# 접근법 자체는 동일함 다만 제어문 사용에서 훨씬 깔끔함
def solution(want, number, discount):
    answer = 0
    dic = dict(zip(want, number))

    # 행사 종료일까지 10일 미만으로 남았다면 의미 없으므로 범위는 len(discount)-9
    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]): 
            answer += 1

    return answer