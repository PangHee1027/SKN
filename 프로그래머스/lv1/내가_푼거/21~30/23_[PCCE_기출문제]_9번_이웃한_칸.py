def get_color(board, h, w) :
    if h < 0 or w < 0 or h >= len(board) or w >= len(board[h]) :
        return
    return board[h][w]

def solution(board, h, w):
    current_color = get_color(board, h, w)
    neighbor = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    answer = 0

    for i in neighbor :
        if get_color(board, h + i[0], w + i[1]) == current_color :
            answer += 1
    
    return answer

# print(solution([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]], 0, 1))