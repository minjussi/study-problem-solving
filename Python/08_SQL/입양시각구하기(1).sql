-- having절로 시간대 설정하기
-- hour 함수의 사용

SELECT HOUR(datetime) as hour, COUNT(datetime)
FROM animal_outs
GROUP BY hour
HAVING hour >= 9 and hour <=19
ORDER BY hour
