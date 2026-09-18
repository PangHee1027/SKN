def solution(N, stages):
    fail_rate = dict()
    answer = list()
    users = len(stages)

    for i in range(1, N+2):
        fail_rate[i]=list()
    for s in stages:
        fail_rate[s].append(1)
    for i in range(1, N+2):
        temp=len(fail_rate[i])
        if(temp == 0):
            fail_rate[i]=0
        else:
            fail_rate[i] = temp/float(users)
        users -= temp

    del(fail_rate[N+1])
    for stage_number in sorted(fail_rate, key=fail_rate.get, reverse=True):
        answer.append(stage_number)
    return answer