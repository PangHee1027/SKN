def solution(s) : 
    def rotate(string) :
        return string[1:] +string[0]
    
    def is_correct(string) :
        big, mid, small = 0, 0, 0
        stack = []
        for c in string :
            match c :
                case '(' :
                    small += 1
                case ')' :
                    small -= 1
                    if stack and stack[-1] == '(' :
                        stack.pop()
                        continue
                    return False
                case '{' :
                    mid += 1
                case '}' :
                    mid -= 1
                    if stack and stack[-1] == '{' :
                        stack.pop()
                        continue
                    return False
                case '[' :
                    big += 1
                case ']' :
                    big -= 1
                    if stack and stack[-1] == '[' :
                        stack.pop()
                        continue
                    return False
            if any(x < 0 for x in (small, mid, big)) :
                return False
            stack.append(c)
        if all(not x for x in (small, mid, big)) :
            return True
        return False
    
    for _ in range(len(s)) :
        if is_correct(s) :
            break
        s = rotate(s)
    else :
        return 0
        
    stack = []
    answer = 0
    
    for c in s :
        stack.append(c) 
        if is_correct(stack) :
            stack = []
            answer += 1
        
    return answer