def solution(n, k):
    def convert(num, base):
        if num == 0:
            return "0"
        digits = "0123456789"
        result = ""
        
        while num > 0:
            num, remainder = divmod(num, base)
            result = digits[remainder] + result
                
        return result
    
    num = convert(n, k)
    nums = [i for i in num.split("0") if i != ""]
    answer = 0

    for number in nums :
        num_int = int(number)

        if num_int == 1 :
            continue
        if num_int == 2 :
            answer += 1
            continue

        for i in range(2, int(num_int ** 0.5) + 1) :
            if num_int % i == 0 :
                break
        else :
            answer += 1
    
    return answer

print(solution(110011, 10))