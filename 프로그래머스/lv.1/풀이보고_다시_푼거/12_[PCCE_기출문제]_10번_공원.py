def can_place_mat(park, size):
    # 공원의 행(row)와 열(col) 길이
    rows, cols = len(park), len(park[0])

    # park에서 주어진 size의 돗자리를 놓을 수 있는지 확인
    for i in range(rows - size + 1):
        for j in range(cols - size + 1):
            # size x size 크기의 공간이 모두 '-1'인지 확인
            # all() 함수를 처음 알았네
            # all() = 조건문1 and 조건문2 and ...... and 마지막 조건문
            if all(park[x][y] == '-1' for x in range(i, i + size) for y in range(j, j + size)):
                return True
    return False

def solution(mats, park):
    # 돗자리 크기 내림차순으로 정렬
    mats.sort(reverse=True)

    # 각 돗자리 크기에 대해 놓을 수 있는지 확인
    for size in mats:
        if can_place_mat(park, size):
            return size

    return -1