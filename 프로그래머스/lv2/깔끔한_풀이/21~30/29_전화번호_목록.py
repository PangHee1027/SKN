def solution(phone_book):
    # 1. 사전순 정렬
    phone_book.sort()
    
    # 2. 인접한 두 번호(p1, p2)를 비교하여 접두어 여부 검사
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
            
    return True