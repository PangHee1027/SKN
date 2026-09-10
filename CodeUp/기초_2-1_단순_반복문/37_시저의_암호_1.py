a = input()
b = []

def caesar(str, key) :
    result = ""
    match str :
        case " " :
            result = " "
        case _ :
            if ord(str) - key < ord("a") :
                result = chr(ord("z") - (ord("a") - (ord(str) - key)) + 1)
            else :
                result = chr(ord(str) - key)
    return result

for i in a :
    b.append(caesar(i, 3))

print("".join(b))
