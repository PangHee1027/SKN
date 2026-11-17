import re

def solution(babbling):
    pattern = 'aya|ye|woo|ma'
    answer = 0
    
    for word in babbling :
        masked_word = re.sub(pattern, '', word)
        if re.search('ayaaya|yeye|woowoo|mama', word) :
            continue
        if not masked_word :
            answer += 1
    return answer