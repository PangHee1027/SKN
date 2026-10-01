def solution(phone_book):
    phone_book.sort()
    for i, phone in enumerate(phone_book) :
        if i < len(phone_book) - 1 and phone_book[i + 1].startswith(phone) :
            return False
    return True

print(solution(["0", "10"]))