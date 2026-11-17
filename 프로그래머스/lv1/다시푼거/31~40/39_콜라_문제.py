def solution(a, b, n) :
    service = 0
    while n >= a :
        div, n = divmod(n, a)
        cur_service = div * b
        service += cur_service
        n += cur_service
    return service