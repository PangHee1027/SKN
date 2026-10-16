def solution(name):
    alphabets = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4,
                 "F" : 5,"G" : 6, "H" : 7, "I" : 8, "J" : 9,
                 "K" : 10, "L" : 11, "M" : 12, "N" : 13, "O" : 12,
                 "P" : 11, "Q" : 10, "R" : 9, "S" : 8, "T" : 7,
                 "U" : 6, "V" : 5, "W" : 4, "X" : 3, "Y" : 2, "Z" : 1
                 }
    answer = 0
    len_name = len(name) - 1
    min_left_right = [len_name]
    a_range = []
    a_idx = []

    if all (x == "A" for x in name) :
        return 0

    for i, s in enumerate(name) :
        answer += alphabets[s]
        if s == "A" :
            a_idx.append(i)
        else :
            if a_idx :
                a_range.append((a_idx[0], a_idx[-1]))
                a_idx = []
    if a_idx :
        a_range.append((a_idx[0], a_idx[-1]))

    for start, last in a_range :
        left_right = (start - 1) * 2 + len_name - last
        right_left = (len_name - last) * 2 + start - 1
        if start == 0 :
            left_right = len_name - last
        if last == len_name :
            right_left = start - 1
        min_left_right += [left_right, right_left]

    return answer + min(min_left_right)

print(solution("JEROEN")) # 56
print(solution("JAN")) # 23
print(solution("ABAAAB")) # 5