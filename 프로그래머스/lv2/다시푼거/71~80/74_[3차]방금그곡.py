import re

def convert(time) :
    hour, minute = map(int, time.split(':'))
    return hour * 60 + minute

def solution(m, musicinfos) :
    pattern = '(C#|D#|F#|G#|A#|A|B|C|D|E|F|G)'
    m = re.findall(pattern, m)
    for i, musicinfo in enumerate(musicinfos) :
        start, end, title, code = musicinfo.split(',')
        song_length = convert(end) - convert(start)
        code = re.findall(pattern, code)
        code *= 1000
        code = code[:song_length]
        print(code)
        musicinfos[i] = [song_length, title, code]
    
    musicinfos.sort(key = lambda x : -x[0])
    
    for _, title, code in musicinfos :
        if any(code[i : i + len(m)] == m for i in range(len(code) - len(m) + 1)) :
            return title
    return '(None)'