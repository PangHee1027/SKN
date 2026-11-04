def solution(s) :
    answer = []
    for string in s :
        count = 0
        stack = []
        for n in string :
            stack.append(n)
            if len(stack) < 3 :
                continue
            while stack[-3:] == ['1', '1', '0'] :
                stack.pop()
                stack.pop()
                stack.pop()
                count += 1
        string = "".join(stack)
        if '0' not in string :
            answer.append('110' * count + string)
        else :
            for i in range(len(string) - 1, -1, -1) :
                if string[i] == '0' :
                    answer.append(string[:i + 1] + '110' * count + string[i + 1 :])
                    break
    return answer

print(solution(["1110","100111100","0111111010"])) # ["1101","100110110","0110110111"]