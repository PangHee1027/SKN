def return_signal (signal) :
    return_signal = []
    for i in range(signal[0]) :
        return_signal.append("g")
    for i in range(signal[1]) :
       return_signal.append("y") 
    for i in range(signal[2]) :
       return_signal.append("r")
    return return_signal

def solution(signals = 0):
    answer = 0
    if not signals :
        return -1
    seconds = 0
    for i in range(len(signals)) :
        signals[i] = return_signal(signals[i])
    signal_times = [0 for i in range(len(signals))]
    while True :
        for i in range(len(signals)) :
            if signals[i][signal_times[i]] != "y" :
                for j in range(len(signal_times)) :
                    signal_times[j] += 1
                    if signal_times[j] == len(signals[j]) :
                        signal_times[j] = 0
                break
        else :
            seconds += 1
            answer = seconds
            break
        seconds += 1
        sum = 0
        for i in signal_times :
            sum += i
        if sum == 0 :
            return - 1
    return answer
