def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(w, h):
    # 전체 사각형 넓이
    extent = w * h
    
    # 가로, 세로의 최대공약수 구하기
    gcd = get_gcd(w, h)
    a, b = w // gcd, h // gcd
    
    # 대각선이 지나가는 사각형 개수 공식 적용
    diagonal = a + b - 1
    
    return extent - (diagonal * gcd)