# 시간 초과

def solution(ingredient):
    ingredient = "".join([str(i) for i in ingredient]) 
    answer = 0
    while True :
        ingredient = ingredient.split('1231', 1)
        if len(ingredient) == 1 :
            break
        answer += 1
        ingredient = "".join(ingredient)
    return answer

# print(solution([1,2,1,2,3,1,3,1,2,3,1,2,3,1]))
