a, b, c = input().split()
triangle = [int(a), int(b), int(c)]
triangle.sort()

print("yes" if triangle[2] < triangle[0] + triangle[1] else "no")
