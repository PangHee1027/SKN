a = input()
b = []

def caesar(str) :
    result = ""
    match str :
        case " " :
            result = " "
        case "x" :
            result = chr(ord("a"))
        case "y" :
            result = chr(ord("a") + 1)
        case "z" : 
            result = chr(ord("a") + 2)
        case _ :
            result = chr(ord(str) + 3)
    return result


for i in a :
    b.append(caesar(i))

print("".join(b))
