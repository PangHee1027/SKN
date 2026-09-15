# 이미 시간 초과가 나는 상황인 상태로 제미나이한테 도움 받음
# 굴러는 가는데 시간복잡도가 너무 높은 듯
# 이분 탐색 사용할 것
def solution(a, b, g, s, w, t):
    answer = 0
    while True :
        if a <= 0 and b <= 0 :
            break
        answer += 1
        for i in range(len(g)) :
            if answer % (t[i] * 2) == t[i] :
                if a > 0 or (a - g[i] >= 0 and w[i] >= g[i]) :
                    if g[i] - w[i] >= 0 and a - w[i] > 0 :
                        a -= w[i]
                        g[i] -= w[i]
                    else :
                        a -= g[i]
                        g[i] = 0
                        b -= (w[i] - g[i]) if s[i] != 0 else 0
                else :
                    if s[i] - w[i] >= 0 and b - w[i] > 0 :
                        b -= w[i]
                        s[i] -= w[i]
                    else :
                        b -= s[i]
                        s[i] = 0
    return answer

print(solution(90, 500, [70,70,0],[0,0,500], [100,100,2], [4,8,1]))