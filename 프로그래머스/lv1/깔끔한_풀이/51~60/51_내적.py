def solution(a, b):
    # 대괄호([])를 제거하여 제네레이터식으로 작성
    return sum(i * j for i, j in zip(a, b))