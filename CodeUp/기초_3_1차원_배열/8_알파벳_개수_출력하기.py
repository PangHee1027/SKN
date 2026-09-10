alphabet = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

str = input()

for i in range(len(str)) :
    now = ord(str[i])
    if 122 >= now >= 97 :
        alphabet[now - 97] += 1

for i in range(len(alphabet)) :
    print(f"{chr(i + 97)}:{alphabet[i]}")
