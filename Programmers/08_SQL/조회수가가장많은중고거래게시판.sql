-- 문자열 연결 시에는 concat 함수 사용 !
-- subquery의 사용

SELECT concat('/home/grep/src/', file.board_id, '/', file.file_id, file.file_name, file.file_ext) AS file_path
FROM used_goods_board AS board join used_goods_file AS file on board.board_id = file.board_id
WHERE board.views = ( -- 최대 조회수를 찾고 싶은 거니까
                      -- views가 어떤 값인 걸 내가 걸러낼거야? 에 대한 답
    SELECT max(views) -- max인 것
    FROM used_goods_board
)
ORDER BY file.file_id desc;
