def convert(num, base):
    if num == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result = ""
    while num > 0:
        num, remainder = divmod(num, base)
        result = digits[remainder] + result
    return result

def solution(n, t, m, p):
    game_str = ""
    cur_num = 0
    
    # 1. t * m 길이 이상이 될 때까지 n진수 문자열 이어 붙이기
    while len(game_str) < t * m:
        game_str += convert(cur_num, n)
        cur_num += 1
        
    # 2. p-1 인덱스부터 m 간격으로 슬라이싱 후 t개만 반환
    return game_str[p - 1 :: m][:t]