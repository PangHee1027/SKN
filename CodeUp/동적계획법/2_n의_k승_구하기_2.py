n, k = map(int, input().split())
mod = 1000000007

def square(n, k) :
    if k == 1 :
        return n
    result = square(n, k // 2) ** 2
    if k % 2 :
        result *= n
    return result % mod

print(square(n, k))
