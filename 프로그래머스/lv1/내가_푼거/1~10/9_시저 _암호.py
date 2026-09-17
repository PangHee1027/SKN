def caesar(str, key) :
    result = ""
    match str :
        case " " :
            result = " "
        case _ :
            if ord(str) + key > ord("z") :
                result = chr(ord("a") + ord(str) + key - ord("z") - 1)
            elif ord("a") + key > ord(str) + key > ord("Z") :
                result = chr(ord("A") + ord(str) + key - ord("Z") - 1)
            else :
                result = chr(ord(str) + key)
    return result

def solution(s, n):
    answer = []

    for i in s :
        answer.append(caesar(i, n))
    answer = "".join(answer)

    return answer
