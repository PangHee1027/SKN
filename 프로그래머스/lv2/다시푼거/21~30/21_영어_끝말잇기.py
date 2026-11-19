def solution(n, words):
    word = set()
    last = ''
    for i, w in enumerate(words) :
        if not last :
            last = w[-1]
            word.add(w)
            continue
        if w in word :
            return [i % n + 1, i // n + 1]
        if w[0] != last :
            return [i % n + 1, i // n + 1]
        last = w[-1]
        word.add(w)
    
    return [0, 0]