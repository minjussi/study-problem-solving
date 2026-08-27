-- 1. 리뷰 많이 쓴 사람만 골라내기
-- 2. 골라낸 다음에 그 사람 이름 찾기
-- DATE_FORMAT(컬럼명, '형식지정 ex. %Y-%m-%d')
-- RANK를 써야하는 이유: 동점 순위 때문에 무조건 RANK 써야 함
-- PARTITION BY + ORDER BY : 내가 지정한 방 안에서 1등 찾기 / ORDER BY: 테이블 전체 1등 찾기

SELECT p.member_name, r.review_text, DATE_FORMAT(r.review_date, '%Y-%m-%d') as review_date
FROM member_profile AS p join rest_review AS r on p.member_id = r.member_id
WHERE p.member_id in (
    SELECT member_id
    FROM (
        SELECT member_id, RANK() OVER (ORDER BY COUNT(*) desc) AS rnk
        FROM rest_review
        GROUP BY member_id
    ) AS grading
    WHERE rnk = 1
)
ORDER BY r.review_date asc, r.review_text asc;
