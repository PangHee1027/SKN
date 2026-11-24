import re

def solution(files):
    original = {i : x for i, x in enumerate(files)}
    pharsing = [[x, i] for i, x in enumerate(files)]
    pattern = re.compile(r'(?P<head>[a-z\-\. ]+)(?P<number>\d+)')
    
    for i, (x, j) in enumerate(pharsing) :
        x = x.lower()
        m = re.search(pattern, x)
        pharsing[i] = [[m.group('head'), int(m.group('number'))], j]
    
    pharsing.sort(key = lambda x : (x[0][0], x[0][1]))
    
    return [original[i] for _, i in pharsing]