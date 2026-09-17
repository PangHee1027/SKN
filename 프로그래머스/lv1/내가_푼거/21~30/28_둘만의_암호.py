alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def solution(s, skip, index):
    answer = ''
    for i in skip :
        alphabet.remove(i)

    secret_alphabet = dict(enumerate(alphabet))
    secret_index = {x : i for i, x in enumerate(alphabet)}
    sar = len(secret_alphabet)

    for i in s :
        answer += secret_alphabet[(secret_index[i] + index) % sar]

    return answer

# print(solution("aukks", "wbqd", 5))