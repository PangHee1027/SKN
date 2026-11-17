import sys
sys.setrecursionlimit(100000)

def solution(num) :
    def collatz(n, count) :
        if n == 1 :
            return count
        if count > 500 :
            return -1
        if n % 2 :
            return collatz(n * 3 + 1 , count + 1)
        else :
            return collatz(n // 2, count + 1)
    return collatz(num, 0)