def solution(n, k, cmd):
    prev = [i - 1 for i in range(n)]
    next = [i + 1 for i in range(n)]
    prev[0], next[-1] = None, None
    current = k
    deleted_index = []
    answer = ['O'] * n

    for c in cmd :
        if c == 'C' :
            pre, nxt = prev[current], next[current]
            deleted_index.append((pre, current, nxt))
            if pre is not None:
                next[pre] = nxt
            if nxt is not None :
                prev[nxt] = pre
                current = nxt
            else :
                current = pre
        elif c == 'Z' :
            pre, curr, nxt = deleted_index.pop()
            if pre is not None:
                next[pre] = curr
            if nxt is not None:
                prev[nxt] = curr
            prev[curr] = pre
            next[curr] = nxt
        else :
            command, idx = c.split()
            count = int(idx)
            if command == 'U' :
                for _ in range(count) :
                    current = prev[current]
            else :
                for _ in range(count) :
                    current = next[current]

    for _, x, _ in deleted_index :
        answer[x] = 'X'
    return "".join(answer)

#print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))