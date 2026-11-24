def solution(n, t, m, p):
    def get_radix_n(n, num) :
        result = ''
        while num >= n :
            num, mod = divmod(num, n)
            result += digits[mod]
        result += digits[num]
        return result[::-1]
    
    digits = '0123456789ABCDEF'
    game = ''
    for i in range(t * m) :
        game += get_radix_n(n, i)
    answer = ''.join(x for i, x in enumerate(game) if i % m == p - 1)[:t]
    return answer