-- CASE-WHEN 문법 기억하기

SELECT 
    board_id, 
    writer_id, 
    title, 
    price, 
    CASE 
        WHEN status = 'RESERVED' THEN '예약중'
        WHEN status = 'DONE' THEN '거래완료'
        ELSE '판매중' 
    END AS status
FROM 
    used_goods_board
WHERE 
    created_date LIKE '2022-10-05%' 
ORDER BY 
    board_id DESC;
