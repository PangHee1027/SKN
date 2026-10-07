from collections import deque

def divide(arr) :
    count_zero = 0
    count_one = 0
    dq = []
    length = len(arr)
    if length == 1 :
        return None, arr[0].count(0), arr[0].count(1)
    half = length // 2
    division = [(0, half, 0, half), (0, half, half, length), (half, length, 0, half), (half, length, half, length)]
    for x1, x2, y1, y2 in division :
        sub_arr = []
        for j in range(x1, x2) :
            row = arr[j][y1 : y2]
            sub_arr.append(row)
        d1_list = sum(sub_arr, [])
        check = sum(d1_list)
        if check == 0 :
            count_zero += 1
        elif check == len(d1_list) :
            count_one += 1
        else :
            dq.append(sub_arr)
    return dq, count_zero, count_one

def check_all_same(arr):
    first = arr[0][0]
    for row in arr:
        for val in row:
            if val != first:
                return False, -1
    return True, first

def solution(arr):
    count_zero = 0
    count_one = 0
    dq = deque([arr])

    while dq :
        cur = dq.popleft()

        is_same, target = check_all_same(cur)
        if is_same:
            if target == 0:
                count_zero += 1
            else:
                count_one += 1
            continue

        l, c0, c1 = divide(cur)
        dq += l
        count_zero += c0
        count_one += c1      

    answer = [count_zero, count_one]
    return answer

print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))