def solution(data, ext, val_ext, sort_by):
    tag = {'code' : 0, 'date' : 1, 'maximum' : 2, 'remain' : 3}
    result = [x for x in data if x[tag[ext]] < val_ext]
    return sorted(result, key = lambda x : x[tag[sort_by]])