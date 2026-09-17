def solution(video_len, pos, op_start, op_end, commands):
    video_len = list(map(int, video_len.split(":")))
    pos = list(map(int, pos.split(":")))
    op_start = list(map(int, op_start.split(":")))
    op_end = list(map(int, op_end.split(":")))
    video_len = 60 * video_len[0] + video_len[1]
    pos = 60 * pos[0] + pos[1]
    op_start = 60 * op_start[0] + op_start[1]
    op_end = 60 * op_end[0] + op_end[1]

    if pos >= op_start and pos <= op_end :
        pos = op_end

    for c in commands :
        match c :
            case "prev" :
                if pos <= 10 :
                    pos = 0
                else :
                    pos -= 10
            case "next" :
                if pos >= video_len - 10 :
                    pos = video_len
                else :
                    pos += 10
        if pos >= op_start and pos <= op_end :
            pos = op_end
            
    answer = format((pos // 60), "02d") + ":" + format(pos % 60, "02d")
    return answer

# print(solution("07:22", "04:05", "00:15", "04:07", ["next"]))