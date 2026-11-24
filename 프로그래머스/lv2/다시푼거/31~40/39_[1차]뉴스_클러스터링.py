from collections import Counter
import re

def solution(str1, str2) :
    s1, s2 = [], []
    str1, str2 = str1.lower(), str2.lower()
    n1, n2 = len(str1), len(str2)
    
    for i in range(n1 - 1) :
        if re.match(r'[a-z]{2}', str1[i : i + 2]) :
            s1.append(str1[i : i + 2])
    for i in range(n2 - 1) :
        if re.match(r'[a-z]{2}', str2[i : i + 2]) :
            s2.append(str2[i : i + 2])
            
    c1, c2 = Counter(s1), Counter(s2)
    intersect, union = c1 & c2, c1 | c2
    print(intersect, union)
    if not union :
        return 65536

    return int(sum(intersect.values()) / sum(union.values()) * 65536)