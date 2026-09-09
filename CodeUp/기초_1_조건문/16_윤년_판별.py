a = int(input())

print("Leap" if (a % 400 == 0 or (a % 4 == 0 and a % 100 != 0)) else "Normal")
