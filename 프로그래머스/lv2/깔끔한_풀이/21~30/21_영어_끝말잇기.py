def solution(n, words):
    seen = set()

    for i, word in enumerate(words):
        # 1. 이전 단어의 끝 글자로 시작하지 않거나, 이미 말했던 단어인 경우
        if (i > 0 and words[i - 1][-1] != word[0]) or word in seen:
            return [i % n + 1, i // n + 1]
        
        seen.add(word)

    # 탈락자가 나오지 않은 경우
    return [0, 0]