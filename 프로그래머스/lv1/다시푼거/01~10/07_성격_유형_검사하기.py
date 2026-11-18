def solution(survey, choices) :
    score = [0, 3, 2, 1, 0, -1, -2, -3]
    case = ['RT', 'CF', 'JM', 'AN']
    rt, cf, jm, an = 0, 0, 0, 0
    for s, c in zip(survey, choices) :
        match s :
            case "RT" :
                rt += score[c]
            case "TR" :
                rt -= score[c]
            case "FC" :
                cf -= score[c]
            case "CF" :
                cf += score[c]
            case "MJ" :
                jm -= score[c]
            case "JM" :
                jm += score[c]
            case "AN" :
                an += score[c]
            case "NA" :
                an -= score[c]
    answer = ''
    for i, s in enumerate([rt, cf, jm, an]) :
        answer += case[i][0 if s >= 0 else 1]
    return answer