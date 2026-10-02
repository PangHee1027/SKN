def solution(cacheSize, cities):
    cache = []
    answer = 0
    for c in cities :
        city = c.upper()
        if city and city in cache :
            answer += 1
            cache.remove(city)
            cache.append(city)
            continue
        if len(cache) < cacheSize :
            cache.append(city)
            answer += 5
            continue
        else :
            if cache :
                cache.pop(0)
            if len(cache) < cacheSize :
                cache.append(city)
            answer += 5
    
    return answer

print(solution(3, ["a", "b", "a", "c", "d", "a"]))
