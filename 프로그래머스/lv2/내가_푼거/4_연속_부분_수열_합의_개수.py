def solution(elements):
    s = set()
    l = []

    for i in range(len(elements)) :
        for j in range(len(elements)) :
            if i + j + 1 <= len(elements) :
                s.add(sum(elements[i:i + j + 1]))
            else :
                s.add(sum(elements[i:]) + sum(elements[:(i + j) % len(elements) + 1]))
                
    return len(s)

# print(solution([7,9,1,1,4]))