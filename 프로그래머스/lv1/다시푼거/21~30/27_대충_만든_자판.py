def solution(keymap, targets):
    answer = []
    for target in targets :
        result = []
        for c in target :
            cur_result = []
            for km in keymap :
                cur = km.find(c)
                if cur == -1 :
                    continue
                cur_result.append(cur)
            if not cur_result :
                result.append(-1)
                break
            result.append(min(cur_result) + 1)
        if any(x == -1 for x in result) :
            answer.append(-1)
        else :
            answer.append(sum(result))
        
    return answer