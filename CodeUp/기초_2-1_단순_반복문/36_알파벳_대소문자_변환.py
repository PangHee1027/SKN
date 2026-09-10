a = input()

def change_char (str) :
    list = []
    for i in range(len(str)) :
        if ord("a") <= ord(str[i]) <= ord("z") :
            list.append(chr(ord(str[i]) - 32))
        elif ord("A") <= ord(str[i]) <= ord("Z") :
            list.append(chr(ord(str[i]) + 32))
        else :
            list.append(str[i])
    return "".join(list)

print(change_char(a))
