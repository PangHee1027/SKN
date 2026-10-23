from collections import defaultdict

def solution(genres, plays):
    genre_total_play = defaultdict(int)  # 장르별 총 재생 횟수
    genre_songs = defaultdict(list)      # 장르별 곡 정보 (재생 횟수, 고유 번호)

    # 1. 데이터 분류 및 총합 계산
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_total_play[genre] += play
        genre_songs[genre].append((play, i))

    # 2. 장르 총 재생 횟수 기준 내림차순 정렬
    sorted_genres = sorted(genre_total_play.keys(), key=lambda g: genre_total_play[g], reverse=True)

    answer = []

    # 3. 각 장르별로 노래 정렬 후 상위 2개 추출
    for genre in sorted_genres:
        # 조건: 1. 재생 횟수 내림차순 (-x[0]) / 2. 고유 번호 오름차순 (x[1])
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        
        # 최대 2개까지 고유 번호(인덱스)만 결과에 추가
        for play, i in sorted_songs[:2]:
            answer.append(i)

    return answer