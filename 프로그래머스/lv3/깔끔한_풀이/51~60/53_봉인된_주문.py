def solution(n, bans):
    def string2int(s):
        result = 0
        for char in s:
            result = result * 26 + (ord(char) - ord('a') + 1)
        return result

    def int2string(num):
        result = []
        while num > 0:
            num, remainder = divmod(num - 1, 26)
            result.append(chr(ord('a') + remainder))
        return "".join(reversed(result))

    # 길이를 우선으로 하고 사전 순으로 정렬
    sorted_bans = sorted(bans, key=lambda x: (len(x), x))

    for ban in sorted_bans:
        if string2int(ban) <= n:
            n += 1
        else:
            break

    return int2string(n)