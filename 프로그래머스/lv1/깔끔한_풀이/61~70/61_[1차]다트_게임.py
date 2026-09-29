import re

def solution(dartResult):
    # (\d+): 숫자, ([SDT]): 보너스, ([*#]?): 옵션(있거나 없음)
    tokens = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)
    
    scores = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    for num, b, opt in tokens:
        score = int(num) ** bonus[b]
        if opt == '*':
            score *= 2
            if scores:
                scores[-1] *= 2
        elif opt == '#':
            score *= -1
        scores.append(score)
        
    return sum(scores)