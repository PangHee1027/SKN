def solution(n, tops) :
    a = [0] * n
    b = [0] * n

    a[0] = 1
    b[0] = 3 if tops[0] == 1 else 2

    for i in range(1, n) :
        if not tops[i] :
            a[i] = (a[i - 1] + b[i - 1]) % 10007
            b[i] = (a[i - 1] + 2 * b[i - 1]) % 10007
        else :
            a[i] = (a[i - 1] + b[i - 1]) % 10007
            b[i] = (2 * a[i - 1] + 3 * b[i - 1]) % 10007
    return (a[-1] + b[-1]) % 10007

print(solution(2, [0, 1]))