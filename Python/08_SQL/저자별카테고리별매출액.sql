-- multiple join 활용하기

SELECT a.author_id, a.author_name, b.category, SUM(s.sales*b.price) as total_sales
FROM book as b 
join author as a on a.author_id = b.author_id 
join book_sales as s on b.book_id = s.book_id
WHERE s.sales_date like '2022-01%'
GROUP BY a.author_name, b.category
ORDER BY a.author_id asc, b.category desc;
