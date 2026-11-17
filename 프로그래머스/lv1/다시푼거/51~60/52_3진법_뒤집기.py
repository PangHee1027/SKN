def solution(n):
    convert = ''
    while n :
        n, mod = divmod(n, 3)
        convert += str(mod)
    return int(convert, 3)