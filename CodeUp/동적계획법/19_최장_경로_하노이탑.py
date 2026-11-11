n = int(input())

col = ['A', 'B', 'C']

def long_hanoi(n, start, end, via) :
    if n == 1:
        return [f'{n} : {col[start]}->{col[via]}', f'{n} : {col[via]}->{col[end]}']
    return (
        long_hanoi(n - 1, start, end, via) + 
        [f'{n} : {col[start]}->{col[via]}'] + 
        long_hanoi(n - 1, end, start, via) + 
        [f'{n} : {col[via]}->{col[end]}'] + 
        long_hanoi(n - 1, start, end, via)
    )

actions = long_hanoi(n, 0, 2, 1)
for action in actions :
    print(action)

print(len(actions))