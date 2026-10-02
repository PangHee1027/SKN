def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_multiset = {}
    str2_multiset = {}
    for i in range(len(str1) - 1) :
        string = str1[i : i + 2]
        if string.isalpha() :
            str1_multiset[string] = str1_multiset.get(string, 0) + 1
    for i in range(len(str2) - 1) :
        string = str2[i : i + 2]
        if string.isalpha() :
            str2_multiset[string] = str2_multiset.get(string, 0) + 1
    if len(str1_multiset) == len(str2_multiset) == 0 :
        return 65536
    union = 0
    intersection = 0
    keys = set(str1_multiset.keys()).union(set(str2_multiset.keys())) 
    for key in keys :
        str1_count = str1_multiset.get(key, 0)
        str2_count = str2_multiset.get(key, 0)
        union += max(str1_count, str2_count)
        intersection += min(str1_count, str2_count)

    return int(intersection / union * 65536)

print(solution("aa1+aa2", "AAAA12"))