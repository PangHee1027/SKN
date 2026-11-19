from collections import Counter

def solution(want, number, discount) :
    want_dict = dict(zip(want, number))
    count = Counter(want_dict)
    n = len(discount)
    answer = 0
    for i in range(n - 9) :
        if count == Counter(discount[i : i + 10]) :
            answer += 1
    return answer