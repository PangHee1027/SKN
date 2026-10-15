def convert_time(string_time) :
    hour, minute = map(int, string_time.split(":"))
    return (hour * 60 + minute) % 1440

def solution(plans):
    answer = []
    stack = []
    plans.sort(key = lambda x : x[1])

    for i, plan in enumerate(plans) :
        plans[i][1] = convert_time(plan[1])
        plans[i][2] = int(plan[2])

    for time in range(plans[0][1], plans[-1][1] + 1) :
        if stack and stack[-1][1] == 0 :
            answer.append(stack[-1][0])
            stack.pop()
        for subject, start, playtime in plans :
            if start == time :
                stack.append([subject, playtime])
                continue
        if stack :
            stack[-1][1] -= 1

    while stack :
        cur = stack.pop()
        answer.append(cur[0])
        
    return answer

print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]])) # ["korean", "english", "math"]
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]])) # ["science", "history", "computer", "music"]
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]])) # ["bbb", "ccc", "aaa"]