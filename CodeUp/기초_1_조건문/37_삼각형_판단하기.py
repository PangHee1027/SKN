a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
triangle = [a, b, c]
triangle.sort()
a, b, c = triangle[0], triangle[1], triangle[2]
result = ""

if (a + b <= c) :
    result = "삼각형아님"
elif (a == b == c) :
    result = "정삼각형"
elif (a == b or a == c or b == c) :
    result = "이등변삼각형"
elif (a ** 2 + b ** 2 == c ** 2) :
    result = "직각삼각형"
else :
    result = "삼각형"

print(result)
