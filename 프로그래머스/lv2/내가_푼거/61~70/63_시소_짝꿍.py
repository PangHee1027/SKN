from collections import Counter

def solution(weights):
    answer = 0

    count = Counter(weights)
    count_key = count.keys()

    for key in count_key :
        cur = count[key]
        answer += cur * (cur - 1) // 2
        if key % 2 == 0 :
            answer += count.get(key // 2 * 3, 0) * cur
        answer += count.get(key * 2, 0) * cur
        if key % 3 == 0 :
            answer += count.get(key // 3 * 4, 0) * cur

    return answer

print(solution([100,180,360,100,270]))