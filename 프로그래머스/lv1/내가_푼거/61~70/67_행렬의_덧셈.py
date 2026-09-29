import numpy as np

def solution(arr1, arr2):
    return (np.array(arr1) + np.array(arr2)).tolist()

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))