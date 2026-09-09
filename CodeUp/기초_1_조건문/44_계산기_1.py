a = input()
num1 = []
num2 = []
calc = "0"
result = 0

for i in a :
    if calc == "0" :
        if i == "+" or i == "-" or i == "*" or i == "/" :
            calc = i
        else :
            num1.append(i)
    else :
        num2.append(i)

num1 = int("".join(num1))
num2 = int("".join(num2))

match calc :
    case "+" :
        result = num1 + num2
    case "-" :
        result = num1 - num2
    case "*" :
        result = num1 * num2
    case "/" :
        result = format(1.0 * num1 / num2, "0.2f")

print(result)
