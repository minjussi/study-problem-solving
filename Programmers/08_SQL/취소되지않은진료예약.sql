--이중으로 join을 써야하기 때문에 from 절에서 가상 테이블 먼저 만들고, 다시 조회
--뼈대 먼저 잡고, 어떻게 진행해나가야할지 판단한 다음, 코드 작성하기 (어떤 걸 출력해야하는지 명확히 파악 -> join을 효과적으로 해야 실수할 확률 떨어짐)
--일반 컬럼은 as 안 해도 자동으로 apnt_ymd처럼 세팅 됨
--그러나!! sum(), count() 같은 것들은 as로 지정 필수!!

SELECT apnt.apnt_no, apnt.pt_name, apnt.pt_no, doctor.mcdp_cd, doctor.dr_name, apnt.apnt_ymd
FROM (
    SELECT apnt.apnt_ymd as apnt_ymd, apnt.apnt_no as apnt_no, apnt.mddr_id as mddr_id, pt.pt_no as pt_no, pt.pt_name as pt_name
    FROM APPOINTMENT as apnt join PATIENT as pt on apnt.pt_no = pt.pt_no
    WHERE apnt.apnt_ymd like '2022-04-13%' and apnt.apnt_cncl_yn = 'N'
) AS apnt join doctor on apnt.mddr_id = doctor.dr_id
WHERE doctor.mcdp_cd='CS'
ORDER BY apnt.apnt_ymd asc;
