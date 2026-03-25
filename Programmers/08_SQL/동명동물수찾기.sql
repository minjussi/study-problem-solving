-- HAVING의 활용: sql 실행 순서는 from->where->group by->having

SELECT name, COUNT(name) as count
FROM animal_ins
WHERE name is not null   -- 이름이 null이면 필터링
GROUP BY name            -- 이름으로 그룹화
HAVING COUNT(name) >= 2  -- 결과가 2 이상인 것들만 필터링
ORDER BY name
