-- window function
-- NTILE(나누고 싶은 개수) OVER (ORDER BY 컬럼명)

SELECT id, CASE NTILE(4) OVER (ORDER BY size_of_colony desc) 
  WHEN 1 THEN 'CRITICAL' WHEN 2 THEN 'HIGH' WHEN 3 THEN 'MEDIUM' ELSE 'LOW' 
  END AS colony_name
FROM ecoli_data
ORDER BY id asc;

--다른 풀이
SELECT id, CASE
  WHEN quart = 1 THEN 'CRITICAL'
  WHEN quart = 2 THEN 'HIGH'
  WHEN quart = 3 THEN 'MEDIUM'
  ELSE 'LOW'
  END AS colony_name
FROM (
  SELECT id, NTILE(4) OVER (ORDER BY size_of_colony desc) AS quart
  FROM ecoli_data
) AS graded
ORDER BY id asc;
