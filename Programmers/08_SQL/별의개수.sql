-- 2단계: 유저별로 변환된 별 개수를 다 더함
SELECT 
    user_id, 
    SUM(stars) AS total_stars
FROM (
    -- 1단계: 유저+스테이지별 최고 점수 찾고 별로 변환
    SELECT user_id, stage_id, CASE WHEN MAX(scores) <= 100 and MAX(scores)>90 THEN 4
  WHEN MAX(scores) <= 90 and MAX(scores) >80 THEN 3
  WHEN MAX(scores) <= 80 and MAX(scores) > 70 THEN 2
  ELSE 1
  END AS stars
  FROM scores_table
  GROUP BY user_id, stage_id
) AS stage_max_table
GROUP BY user_id;
