def solution(wallpaper) :
    x_idx, y_idx = [], []
    n, m = len(wallpaper), len(wallpaper[0])
    
    for i in range(n) :
        for j in range(m) :
            if wallpaper[i][j] == '#' :
                x_idx.append(i)
                y_idx.append(j)
    
    return [min(x_idx), min(y_idx), max(x_idx) + 1, max(y_idx) + 1]