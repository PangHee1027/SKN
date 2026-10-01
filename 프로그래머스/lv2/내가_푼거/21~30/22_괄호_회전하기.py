def solution(s):
    def is_correct(s) :
        stack = []
        for c in s :
            match c :
                case "]" :
                    if stack and stack[-1] == "[" :
                        stack.pop()
                    else :
                        return False
                case "}" :
                    if stack and stack[-1] == "{" :
                        stack.pop()
                    else :
                        return False
                case ")" :
                    if stack and stack[-1] == "(" :
                        stack.pop()
                    else :
                        return False
                case _ :
                    stack.append(c)
        if stack :
            return False
            
        return True
    
    answer = 0
    for i in range(len(s)) :
        if is_correct(s) :
            answer += 1
        s = s[1:] + s[0]
    return answer

print(solution("{(})"))
