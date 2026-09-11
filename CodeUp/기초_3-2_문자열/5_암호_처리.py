a = input()

print("".join([chr(ord(c) + 2) for c in a]))
print("".join([chr((ord(c) * 7) % 80 + 48) for c in a]))
