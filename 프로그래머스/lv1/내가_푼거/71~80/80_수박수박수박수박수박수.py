def solution(n):
    watermelon = ['수', '박']
    return "".join([watermelon[i % 2] for i in range(n)])