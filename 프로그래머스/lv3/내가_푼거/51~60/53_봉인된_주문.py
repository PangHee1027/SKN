import string

def solution(n, bans) :
    def string2int(string) :
        result = 0
        n = len(string)
        for i, s in enumerate(string) :
            result += 26 ** (n - 1 - i) * alphabet_dict[s]
        return result

    def int2string(num) :
        result = ""
        while num > 0:
            num, remainder = divmod(num, 26)
            if not remainder :
                num -= 1
            result = alphabet[remainder] + result
                        
        return result

    alphabet = string.ascii_lowercase
    alphabet_dict = {x : i + 1 for i, x in enumerate(alphabet)}
    alphabet = alphabet[-1] + alphabet[:-1]
    bans.sort(key = lambda x : (len(x), x))

    for ban in bans :
        if string2int(ban) <= n :
            n += 1
        else :
            break
    
    return int2string(n)

print(solution(30, ["d", "e", "bb", "aa", "ae"]))