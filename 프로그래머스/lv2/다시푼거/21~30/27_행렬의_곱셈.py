import numpy as np

def solution(arr1, arr2):
    a1, a2 = np.array(arr1), np.array(arr2)
    result = np.dot(a1, a2).tolist()
    return result