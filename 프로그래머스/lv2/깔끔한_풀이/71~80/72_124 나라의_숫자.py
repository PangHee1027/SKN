def solution(n):
    digits = "412"
    result = []
    
    while n > 0:
        n, remainder = divmod(n, 3)
        if remainder == 0:
            n -= 1
        result.append(digits[remainder])
        
    # 뒤에서부터 채워졌으므로 역순으로 뒤집은 뒤 문자열로 결합
    return "".join(reversed(result))