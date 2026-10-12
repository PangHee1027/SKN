import heapq

def convert(time_string):
    hour, minute = map(int, time_string.split(":"))
    return hour * 60 + minute

def solution(book_time):
    # 1. 시간을 분 단위로 변환 후, 시작 시간 기준으로 오름차순 정렬
    booking = []
    for start, end in book_time:
        booking.append((convert(start), convert(end) + 10))
    booking.sort(key=lambda x: x[0])
    
    # 2. 최소 힙(Heap)을 사용하여 각 방의 퇴실 시간을 관리
    rooms = []
    
    for start, end in booking:
        # 이미 가장 빨리 끝나는 방이 있고, 그 방의 퇴실 시간보다 현재 예약의 시작 시간이 크거나 같다면
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms) # 기존 방 재사용 (해당 방의 퇴실 시간 갱신을 위해 제거)
        
        # 새로운 퇴실 시간(또는 연장된 퇴실 시간)을 힙에 추가
        heapq.heappush(rooms, end)
        
    # 힙에 남아있는 방의 개수가 필요한 최소 객실 수
    return len(rooms)