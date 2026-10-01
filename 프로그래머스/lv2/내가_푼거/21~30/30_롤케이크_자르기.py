from collections import Counter

def solution(topping):
    answer = 0
    set1 = set()
    cnt = dict(Counter(topping))

    for v in topping :
        set1.add(v)
        cnt[v] -= 1
        if cnt.get(v) == 0 :
            cnt.pop(v)
        if len(set1) == len(cnt) :
            answer += 1
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))