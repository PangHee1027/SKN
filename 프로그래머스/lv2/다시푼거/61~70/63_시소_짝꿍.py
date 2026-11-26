from collections import Counter

def solution(weights):
    counter = Counter(weights)
    answer = 0
    
    for weight in counter.keys() :
        count = counter[weight]
        if count >= 2 :
            answer += count * (count - 1) // 2
        for pair in counter.keys() :
            if pair == weight :
                continue
            if pair == 2 * weight :
                answer += count * counter[pair]
            elif 2 * pair == 3 * weight :
                answer += count * counter[pair]
            elif 3 * pair == 4 * weight :
                answer += count * counter[pair]
                
    return answer