def solution(n, words) :
    word_dict = {}
    
    for i, word in enumerate(words) :
        turns = [i % n + 1, i // n + 1]
        if word_dict.get(word) :
            break
        if i > 0 and words[i - 1][-1] != word[0] :
            break
        word_dict[word] = 1
    else :
        return [0, 0]

    return turns

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
