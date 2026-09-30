def solution(n):
    b_n = f"0{n:b}"
    shift = len(b_n)
    for i in range(shift, 0, -1) :
        if b_n[i - 1 : i + 1] == "01" :
            shift = i - 1
            break
    b_answer = f"0b{b_n[:shift]}10{"".rjust(b_n[shift + 2:].count("1"), "1").zfill(len(b_n[shift + 2:]))}"
    return int(b_answer, 2)

print(solution(15))