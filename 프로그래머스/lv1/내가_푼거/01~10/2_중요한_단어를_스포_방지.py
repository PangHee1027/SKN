def is_change (count, range) :
    result = ""
    for i, j in range :
        if i <= count <= j :
            result = True
            break
        else :
            result = False
    return result

def solution(message, spoiler_ranges) :
    result = 0
    spoiler_message = []
    non_spoiler_message = []
    current = []
    check = False

    for i in range(len(message)) :
        # 공백이고 스포일러 단어인 경우
        if message[i] == " " and check :
            spoiler_message.append("".join(current))
            current = []
            check = False
        # 공백이고 스포일러 단어가 아닌경우
        elif message[i] == " " and not check :
            non_spoiler_message.append("".join(current))
            current = []
            check = False
        # 맨 처음 공백임
        elif message[i] == " " and i == 0 :
            pass
        elif i == len(message) - 1 :
            current.append(message[i])
            if check :
                spoiler_message.append("".join(current))
            else :
                non_spoiler_message.append("".join(current))
        # 공백이 아님
        else :
            check = is_change(i, spoiler_ranges) or check
            current.append(message[i])

    spoiler_message = set(spoiler_message)
    non_spoiler_message = set(non_spoiler_message)

    for i in spoiler_message :
        if not (i in non_spoiler_message) :
            result += 1
    return result

print(solution(	"my phone number is 01012345678 and may i have your phone number", [[5, 5], [25, 28], [34, 40], [53, 59]]))