width , height, bit = input().split()
width , height, bit = int(width) , int(height), int(bit)

def picture_require_MB(w, h, b) :
    result = format(w * h * b * 1.0 / 8 / 1024 / 1024, "0.2f")
    return result

print(f"{picture_require_MB(width, height, bit)} MB")
