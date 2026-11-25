def solution(record):
    result = []
    log = []
    uid = {}
    action = {'Enter' : '님이 들어왔습니다.', 'Leave' : '님이 나갔습니다.'}
    
    for r in record :
        r = r.split()
        if len(r) == 3 :
            uid[r[1]] = r[2]
        if r[0] in ('Enter', 'Leave') :
            log.append(r[:2])
    
    return [f'{uid[u]}{action[a]}' for a, u in log]