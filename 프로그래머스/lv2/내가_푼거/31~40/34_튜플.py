def solution(s):
    s = s.replace("{{", "").replace("}}", "")
    ls = s.split("},{")
    for i, l in enumerate(ls) :
        ls[i] = list(map(int, l.split(",")))
    ls.sort(key = lambda x : len(x))
    answer = []
    for i, l in enumerate(ls) :
        if i :
            pre = ls[i - 1]
            cur = [x for x in l if x not in pre]
            print(cur)
            answer.append(cur[0])
        else :    
            answer.append(l[0])
    return answer

# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
# print(solution("{{20,111},{111}}"))
# print(solution("{{123}}"))
# print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))