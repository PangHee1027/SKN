from collections import Counter

def solution(k, tangerine):
    tangerine_dict = dict(Counter(tangerine))
    tangerine_list = sorted(list(tangerine_dict.values()))
    answer = 0
    while k > 0 :
        answer += 1
        k -= tangerine_list.pop()
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))