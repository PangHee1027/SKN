hz , bit, chanels, seconds = input().split()
hz , bit, chanels, seconds = int(hz) , int(bit), int(chanels), int(seconds)

def require_MB(h, b, c, s) :
    result = format(h * b * c * s * 1.0 / 8 / 1024 / 1024, "0.1f")
    return result

print(f"{require_MB(hz, bit, chanels, seconds)} MB")
