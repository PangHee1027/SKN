def solution(word):
    place = [781, 156, 31, 6, 1]
    vowel = {'A' : 0, 'E' : 1, 'I' : 2, 'O' : 3, 'U' : 4}
    return sum(place[i] * vowel[x] + 1 for i, x in enumerate(word))