from functools import lru_cache
from math import isqrt

def solution(n, k) :
    @lru_cache(None)
    def is_prime(num) :
        if num == 1 :
            return False
        qrt_num = isqrt(num)
        for i in range(2, qrt_num + 1) :
            if not num % i :
                return False
        return True
    
    def get_radix_k(k, n) :
        result = ''
        
        while n >= k :
            n, mod = divmod(n, k)
            result += digits[mod]
        result += digits[n]
        
        return result[::-1]
    
    digits = '0123456789'
    answer = 0
    l = [int(x) for x in get_radix_k(k, n).split('0') if x and is_prime(int(x))]
 
    return len(l)