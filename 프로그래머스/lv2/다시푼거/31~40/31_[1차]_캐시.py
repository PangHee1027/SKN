def solution(cacheSize, cities) :
    cache = {}
    result = 0
    for i, city in enumerate(cities) :
        city = city.lower()
        pre = cache.get(city, -float('inf'))
        if city in sorted(cache.keys(), key = lambda x : -cache[x])[:cacheSize] :
            result += 1
        else :
            result += 5
        cache[city] = i
        
    return result