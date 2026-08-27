--반올림하고 싶을 때: round(x, n) 사용 - x를 n 자리까지 나타냄 (세번째 자리에서 반올림->n=2)
--서울에 위치한 식당이므로 '서울%' 무조건 추가!!

SELECT info.rest_id, info.rest_name, info.food_type, info.favorites as favorites, info.address, round(avg(rev.review_score), 2) as score
FROM rest_info as info join rest_review as rev on info.rest_id = rev.rest_id
WHERE info.address like '서울%'
GROUP BY info.rest_id
ORDER BY score desc, favorites desc;
