def solution(arr1, arr2):
    # zip(*arr2)는 arr2의 열(column)들을 하나의 튜플로 묶어줍니다.
    return [
        [sum(a * b for a, b in zip(r1, c2)) for c2 in zip(*arr2)]
        for r1 in arr1
    ]