from collections import deque

def solution(cacheSize, cities):
    # cacheSize가 0이면 모든 조회가 cache miss
    if cacheSize == 0:
        return len(cities) * 5

    cache = deque(maxlen=cacheSize)
    answer = 0

    for c in cities:
        city = c.upper()
        if city in cache:
            # Cache Hit: 실행시간 +1 및 최근 사용 위치로 갱신
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            # Cache Miss: 실행시간 +5 및 캐시에 추가 (자동으로 오래된 항목 밀려남)
            answer += 5
            cache.append(city)

    return answer