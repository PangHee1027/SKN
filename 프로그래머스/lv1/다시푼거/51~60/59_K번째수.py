def solution(array, commands):
    return [sorted(array[start - 1 : end])[idx - 1] for start, end, idx in commands]