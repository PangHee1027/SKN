def solution(n, t, m, p):
    max_length = t * m
    def convert(num, base):
        if num == 0:
            return "0"
        digits = "0123456789ABCDEF"
        result = ""
        
        while num > 0:
            num, remainder = divmod(num, base)
            result = digits[remainder] + result
            
        return result
    
    string = ""
    cur_num = 0
    while len(string) < max_length :
        string += str(convert(cur_num, n))
        cur_num += 1
    answer = [string[i] for i in range(len(string)) if i % m == p - 1]
    return  "".join(answer[:t])

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))