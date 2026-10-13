def solution(expression):
    stack = []
    ex = []
    operations = [("+", "-", "*"), ("+", "*", "-"), ("-", "+", "*"), ("-", "*", "+"), ("*", "-", "+"), ("*", "+", "-")]

    for s in expression :
        if s in ("*", "-", "+") :
            ex.append(int("".join(stack)))
            ex.append(s)
            stack = []
            continue
        stack.append(s)
    ex.append(int("".join(stack)))

    result = []

    for operation in operations :
        cur_ex = [x for x in ex]
        for op in operation :
            while op in cur_ex :
                operand_indx = cur_ex.index(op) - 1
                operand1 = cur_ex.pop(operand_indx)
                _ = cur_ex.pop(operand_indx)
                operand2 = cur_ex.pop(operand_indx)
                match op :
                    case "+" :
                        cur_ex.insert(operand_indx, operand1 + operand2)
                    case "-" :
                        cur_ex.insert(operand_indx, operand1 - operand2)
                    case "*" :
                        cur_ex.insert(operand_indx, operand1 * operand2)
                
        result.append(abs(cur_ex[0]))

    return max(result)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))