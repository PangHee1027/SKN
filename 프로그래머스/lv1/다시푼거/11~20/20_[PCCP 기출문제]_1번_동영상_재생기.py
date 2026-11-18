def t2i(time) :
    m, s = map(int, time.split(':'))
    return m * 60 + s

def i2t(integer) :
    m, s = divmod(integer, 60)
    return str(m).zfill(2) + ':' + str(s).zfill(2)

def solution(video_len, pos, op_start, op_end, commands) :
    video_len, pos, op_start, op_end = map(t2i, (video_len, pos, op_start, op_end))
    for command in commands :
        if op_start <= pos <= op_end :
            pos = op_end
        if command == 'next' :
            pos = min(video_len, pos + 10)
        else :
            pos = max(0, pos - 10)
    if op_start <= pos <= op_end :
            pos = op_end
    
    return i2t(pos)