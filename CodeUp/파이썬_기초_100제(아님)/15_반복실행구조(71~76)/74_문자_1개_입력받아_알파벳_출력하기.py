input_unicode = ord(input().lower())
present_unicode = ord("a")

while (input_unicode >= present_unicode) :
    print(chr(present_unicode), end = " ")
    present_unicode += 1
