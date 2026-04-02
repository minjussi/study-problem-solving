-- WHERE category in (안에 다 넣기) : 이 문법 기억해두기 !! 
-- 순위별로 정렬한 다음에 1인 것만 뽑기

SELECT category, price, product_name
FROM (
    SELECT category, price, product_name, RANK() OVER (PARTITION BY category ORDER BY price desc) as rnk
    FROM food_product
    WHERE category in ('과자', '국', '김치', '식용유')
) AS rank_table
WHERE rnk = 1
ORDER BY price desc;
