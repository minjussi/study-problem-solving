-- 조건이 2개였음
-- 1. 8~10월 총 대여 횟수가 5회 이상
-- 2. 월별 대여 횟수
-- 1번 조건을 먼저 서브쿼리에서 계산한 다음에 2번을 출력하는 것

SELECT 
    month(start_date) as month, car_id, count(car_id) as records
FROM car_rental_company_rental_history
WHERE (
    start_date >= '2022-08-01' AND start_date < '2022-11-01' -- 무조건 연도 비교까지 해줘야함
    AND car_id in ( -- 5회 이상인 car_id부터 뽑기 
        SELECT car_id
        FROM car_rental_company_rental_history
        WHERE start_date >= '2022-08-01' AND start_date < '2022-11-01'
        GROUP BY car_id
        HAVING COUNT(car_id) >= 5
    )
)
GROUP BY month, car_id -- 월이랑 차 번호가 맞아 떨어지는 것들만 묶어서 보여줌 
ORDER BY month asc, car_id desc;
