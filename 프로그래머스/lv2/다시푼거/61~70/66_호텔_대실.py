from collections import defaultdict

def convert(time) :
    hour, minute = map(int, time.split(':'))
    return hour * 60 + minute

def solution(book_time) :
    room = defaultdict(int)
    for i, book in enumerate(book_time) :
        book = list(map(convert, book))
        book[1] += 10
        book_time[i] = book
    
    book_time.sort(key = lambda x : x[0])
    answer = 1
    
    for start, end in book_time :
        for i in range(answer) :
            if room[i] <= start :
                room[i] = end
                break
        else :
            answer += 1
            room[answer - 1] = end
    
    return answer