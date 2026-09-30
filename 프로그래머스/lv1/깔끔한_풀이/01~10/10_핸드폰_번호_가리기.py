def solution(phone_number):
    # 접근 자체는 비슷했는데 문자열 곱셈을 망각하고 있었음
    return "*"*(len(phone_number)-4)+phone_number[-4:]
   