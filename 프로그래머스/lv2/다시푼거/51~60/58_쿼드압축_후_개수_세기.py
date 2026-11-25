import sys
sys.setrecursionlimit(1000000)

def solution(arr) :
    def get_quad(x, y, n) :
        first = arr[x][y]
        for i in range(x, x + n) :
            for j in range(y, y + n) :
                if arr[i][j] != first :
                    half = n //2
                    get_quad(x, y, half)
                    get_quad(x + half, y, half)
                    get_quad(x, y + half, half)
                    get_quad(x + half, y + half, half)
                    return
        answer[first] += 1
    answer = [0, 0]
    
    n = len(arr)

    get_quad(0, 0, n)

    return answer