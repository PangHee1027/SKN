a = input()
result = 0
num_list = []
opr_list = [""]

def is_operator(str) :
    if str == "+" or str == "-" or str == "*" or str == "/" or str == "=" :
        return True

def calculate(num1, opr, num2) :
    result = 0
    match opr :
        case "+" :
            result = num1 + num2
        case "-" :
            result = num1 - num2
        case "*" :
            result = num1 * num2
        case "/" :
            result = num1 / num2
    return int(result)

count = 0

for i in range(len(a) - 1) :
    if not is_operator(a[i]) :
        if count == 0 :
            while (not is_operator(a[i + count])) :
                count += 1
            num_list.append(int("".join(a[i: i + count])))
        else :
            count -= 1
    else :
        opr_list.append(a[i])
        count = 0

result = num_list[0]

for i in range(1, len(num_list)) :
    result = calculate(result, opr_list[i], num_list[i])

print(result)
