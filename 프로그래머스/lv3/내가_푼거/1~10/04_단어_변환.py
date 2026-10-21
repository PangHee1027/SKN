from collections import deque

def solution(begin, target, words) :
    if target not in words :    
        return 0
    
    n = len(begin)

    def can_covert(word, target) :
        count = 0
        for i in range(n) :
            if word[i] != target[i] :
                count += 1
            if count > 1 :
                return False
        return True

    convert_dict = {}

    convert_list = []
    for word in words :
        if can_covert(begin, word) :
            convert_list.append(word)
    convert_dict[begin] = convert_list

    for i in range(len(words)) :
        word = words[i]
        convert_list = []
        for j in range(len(words)) :
            if i == j :
                continue
            if can_covert(word, words[j]) :
                convert_list.append(words[j])
        convert_dict[word] = convert_list

    min_convert = float("inf")
    dq = deque([(begin, 0)])
    visited = {begin}

    while dq :
        cur, count = dq.popleft()
        if cur == target :
            min_convert = min(min_convert, count)
            continue
        for next in convert_dict[cur] :
            if next not in visited :
                visited.add(next)
                dq.append((next, count + 1))

    if min_convert == float("inf") :
        return 0
    
    return min_convert

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))