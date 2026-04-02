--순서: from->where->group by->having->select->order by
--select 절에서만 alias 가능

SELECT users.user_id, users.nickname, SUM(price) as total_sales
FROM used_goods_board AS board join used_goods_user AS users on board.writer_id = users.user_id
WHERE board.status = 'DONE'
GROUP BY users.user_id
HAVING SUM(price) >= 700000 
ORDER BY total_sales asc;
