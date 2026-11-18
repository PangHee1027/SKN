def get_lcm(a, b) :
    multi = a * b
    while b != 0 :
        a, b = b, a % b
    return multi // a

def solution(signals):
    lcm = 1
    dividor = []
    n = len(signals)
    for i, signal in enumerate(signals) :
        lcm = get_lcm(lcm, sum(signal))
        for j in range(2) :
            signal[j + 1] += signal[j]
        signals[i] = signal
        dividor.append(signal[-1])
    for i in range(1, lcm + 1) :
        for j in range(n) :
            if not (signals[j][0] < (i % dividor[j]) <= signals[j][1]) :
                break
        else :
            return i
    return -1