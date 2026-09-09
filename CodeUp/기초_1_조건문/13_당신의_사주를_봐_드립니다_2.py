year, month, date = input().split()
result = "대박" if (((int(year) + int(month) + int(date)) // 100) % 2 == 0) else "그럭저럭"

print(result)
