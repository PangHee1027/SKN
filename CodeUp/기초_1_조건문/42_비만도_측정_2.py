a, b = input().split()
a, b = float(a), float(b)
c = 0
d = 0

def check_bmi(w) :
    if (w <= 10) :
        return "정상"
    elif (20 >= w > 10) :
        return "과체중"
    else :
        return "비만"

if (a < 150) :
    c = a - 100
    d = (b - c) * 100 / c
elif (160 > a >= 150) :
    c = (a - 150) / 2 + 50
    d = (b - c) * 100 / c
else :
    c = (a - 100) * 0.9
    d = (b - c) * 100 / c

print(check_bmi(d))
