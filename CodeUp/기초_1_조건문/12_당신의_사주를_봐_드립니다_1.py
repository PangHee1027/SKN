year, month, date = input().split()
result = "대박" if (str(int(year) - int(month) + int(date))[-1] == "0") else "그럭저럭"

print(result)
