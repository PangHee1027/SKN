from functools import lru_cache
import sys
sys.setrecursionlimit(100000)

def solution(numbers, target) :
    l = len(numbers)
    
    @lru_cache(None)
    def dfs(n, iter) :
        if iter == l :
            if n == target :
                return 1
            else :
                return 0
        return dfs(n + numbers[iter], iter + 1) + dfs(n - numbers[iter], iter + 1)
    
    return dfs(0, 0)