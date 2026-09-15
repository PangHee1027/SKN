# 확실해 내장 함수에 익숙해질 필요도 보인다
# pop() 지정한 인덱스를 제거함
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
