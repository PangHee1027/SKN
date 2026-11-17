def solution(x) :
    return x % sum(int(s) for s in str(x)) == 0