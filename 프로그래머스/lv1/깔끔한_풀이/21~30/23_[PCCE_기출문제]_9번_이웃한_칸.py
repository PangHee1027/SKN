# [보조 함수] 특정 좌표(h, w)의 색상을 안전하게 가져오는 함수
def get_color(board, h, w):
    # h와 w가 보드 범위를 벗어나지 않는 유효한 인덱스인지 확인
    if 0 <= h < len(board) and 0 <= w < len(board[0]):
        return board[h][w]  # 범위 안이면 해당 위치의 색상 반환
    return None             # 범위를 벗어나면 None 반환 (오류 방지)

def solution(board, h, w):
    # 기준이 되는 현재 칸의 색상을 저장
    current_color = board[h][w]
    
    # 상, 하, 좌, 우 이웃 칸으로 이동하기 위한 좌표 변화량 (dh, dw)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 4방향을 순회하며 조건(현재 색상과 동일)을 만족하는 칸의 개수를 합산하여 반환
    return sum(1 for dh, dw in directions if get_color(board, h + dh, w + dw) == current_color)