def solution(s):
    count = 0
    zero = 0
    
    while s != "1":
        count += 1
        ones = s.count("1")
        zero += len(s) - ones
        s = f"{ones:b}"  # 2진수 문자열 변환
        
    return [count, zero]