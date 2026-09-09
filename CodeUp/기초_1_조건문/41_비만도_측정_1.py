a, b = input().split()
a, b = float(a), float(b)
c = (a - 100) * 0.9
d = ((b - c) * 100) / c

def check_bmi(w) :
    if (w <= 10) :
        return "정상"
    elif (20 >= w > 10) :
        return "과체중"
    else :
        return "비만"

print(check_bmi(d))
