# 구조는 잘 잡았으나, 어떤 함수를 사용해야할지 구현 방법을 익히기
# sort 함수는 오로지 리스트에만 사용 가능
# sorted는 모든 자료형에 사용 가능, 사용 후에는 튜플을 반환
# 무조건 오름차순이 기본임 (asc)! 내림차순 하고 싶으면 reverse=True 옵션
# key=lambda x: (기준 값1, 기준 값2) - lambda 함수 사용법 기억하기

def solution(genres, plays):
    answer = []
    genres_dict = {}
    total_plays_dict = {}
    for i in range(len(genres)):
        if genres[i] in genres_dict:
            total_plays_dict[genres[i]] += plays[i]
            genres_dict[genres[i]].append((plays[i], i))
        else:
            total_plays_dict[genres[i]] = plays[i]
            genres_dict[genres[i]] = [(plays[i], i)]
    # 정렬 먼저 (기준은 value 기준)
    # 딕셔너리는 sort 사용 불가
    # sorted를 하고 나면 튜플로 바뀜
    sorted_genres = sorted(total_plays_dict.items(), key=lambda x: x[1], reverse=True)
    for genre, plays in sorted_genres: # 튜플을 반환했기 때문에 (genre, plays) 형태
        # genres_dict[genre]의 값은 리스트니까 sort 사용 가능
        # 재생 수는 내림차순, 고유 번호는 오름차순
        genres_dict[genre].sort(key=lambda x: (-x[0], x[1]))
        for song in genres_dict[genre][:2]:
            answer.append(song[1])
    return answer
