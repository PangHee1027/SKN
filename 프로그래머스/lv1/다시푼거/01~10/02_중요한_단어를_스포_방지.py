from collections import Counter

def solution(message, spoiler_ranges):
    masked = list(message)
    for s, e in spoiler_ranges :
        for i in range(s, e + 1) :
            if masked[i] != ' ':
                masked[i] = '*'
    masked = ''.join(masked).split()
    original = message.split()
    masked_count = Counter(masked)
    original_count = Counter(original)
    spoiler_words = original_count - masked_count
    
    answer = 0
    
    for k in spoiler_words.keys() :
        if k not in masked :
            answer += 1
            
    return answer
