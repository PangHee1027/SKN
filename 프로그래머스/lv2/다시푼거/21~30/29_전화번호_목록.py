def solution(phone_book):
    phone_book.sort(key = lambda x : (x, len(x)))
    n = len(phone_book)
    
    for i in range(n - 1) :
        a, b = phone_book[i], phone_book[i + 1]
        if b.startswith(a) :
            return False
    return True