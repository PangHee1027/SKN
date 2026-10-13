def solution(n):
    def convert(num):
        digits = "412"
        result = ""
            
        while num > 0:
            num, remainder = divmod(num, 3)
            if not remainder :
                num -= 1
            result = digits[remainder] + result
                
        return result
    
    return convert(n)

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(10))