# 오답

def solution(h1, m1, s1, h2, m2, s2):
    start_time = h1 * 3600 + m1 * 60 + s1
    stop_time = h2 * 3600 + m2 * 60 + s2

    def niddles(time) :
        hour_niddle = (time % 43200) / 43200 * 360
        minute_niddle = (time % 3600) / 3600 * 360
        second_niddle = (time % 60) / 60 * 360

        return [hour_niddle, minute_niddle, second_niddle]

    def alram(time) :
        result = 0
        pre_niddle = []
        for i in range(0, time + 1) :
            cur_niddle = niddles(i)
            if not pre_niddle :
                if cur_niddle[2] == cur_niddle[0] or cur_niddle[1] == cur_niddle[2] :
                    result += 1
                pre_niddle = cur_niddle
                continue
            for i in range(3) :
                if pre_niddle[i] > 350 and cur_niddle[i] < 10 :
                    cur_niddle[i] += 360
            if (pre_niddle[2] < pre_niddle[0] and cur_niddle[2] >= cur_niddle[0]) or pre_niddle[2] < pre_niddle[1] and cur_niddle[2] >= cur_niddle[1] :
                result += 1

            for i in range(3) :
                cur_niddle[i] %= 360

            pre_niddle = cur_niddle

        return result

    return alram(stop_time) - alram(start_time)

#print(solution(0, 0, 0, 23, 59, 59))
#print(solution(12, 0, 0, 12, 0, 30))
print(solution(11, 59, 30, 12, 0, 0))