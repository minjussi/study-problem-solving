-- LEFT JOIN 한 다음, null인 요소를 찾아서 출력
-- LIMIT 3 -> 3개의 행만 출력

SELECT ins.name, ins.datetime 
FROM animal_ins AS ins LEFT JOIN animal_outs AS outs ON ins.animal_id=outs.animal_id
WHERE outs.animal_id is NULL
ORDER BY ins.datetime
LIMIT 3
