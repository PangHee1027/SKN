def solution(string):
    count = 0
    for s in string :
        if s == '(' :
            count += 1
        else :
            count -= 1
        if count < 0 :
            return False
    if count :
        return False
    return True