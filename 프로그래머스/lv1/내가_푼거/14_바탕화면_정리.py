def solution(wallpaper):
    num_of_file = 0
    H, W = len(wallpaper), len(wallpaper[0])

    for i in wallpaper :
        for j in i :
            if j == "#" :
                num_of_file += 1
    start_x, start_y = 0, 0
    last_x, last_y = H, W
    length = (H ** 2) + (W ** 2)
    for i in range(H) :
        for j in range(W) :
            count = 0
            for k in range(i, H) :
                for l in range(j, W) :
                    if wallpaper[k][l] == "#" :
                        count += 1
            if count == num_of_file and length >= ((H - i) ** 2) + ((W - j) ** 2) :
                length = ((H - i) ** 2) + ((W - j) ** 2)
                start_x, start_y = i, j
    for i in range(H - 1, start_x - 1, -1) :
        for j in range(W - 1, start_y - 1, -1) :
            count = 0
            for k in range(i, start_x - 1, - 1) :
                for l in range(j, start_y - 1, -1) :
                    if wallpaper[k][l] == "#" :
                        count += 1
            if count == num_of_file and length >= ((i - start_x) ** 2) + ((j - start_y) ** 2) :
                length = ((i - start_x) ** 2) + ((j - start_y) ** 2)
                last_x, last_y = i + 1, j + 1

    answer = [start_x, start_y, last_x, last_y]
    return answer

# print(solution(["..", "#."]))