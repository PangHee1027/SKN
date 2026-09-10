for i in range(1, 10) :
    row = []
    for j in range(2, 6) :
        row.append(f"{j} x {i} = {j * i:2d}")
    print("\t".join(row))
