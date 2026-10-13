def convert_time(time_string) :
    hour, minute = map(int, time_string.split(":"))
    return hour * 60 + minute

def convert_music(music_string) :
    stack = []
    for code in music_string :
        if code == "#" :
            stack[-1] += code
            continue
        stack.append(code)
    return stack

def convert_music_info(music_info) :
    start, stop, title, music = music_info.split(",")
    start, stop= convert_time(start), convert_time(stop) 
    music = convert_music(music) * (stop - start)
    return {'start' : start, 'stop' : stop, 'length' : stop - start, 'title' : title, 'music' : music[:(stop - start)]}

def solution(m, musicinfos):
    answer = '(None)'
    m = convert_music(m)
    ml = len(m)
    max_length = 0
    for music_info in musicinfos :
        mi = convert_music_info(music_info)
        for j in range(mi['length'] - ml + 1) :
            cur = mi['music'][j : j + ml]
            if cur == m :
                if mi['length'] > max_length :
                    max_length = mi['length']
                    answer = mi['title']
    
    return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))