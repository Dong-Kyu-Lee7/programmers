-- 코드를 입력하세요
SELECT a.APNT_NO, p.PT_NAME, p.PT_NO, a.MCDP_CD, d.DR_NAME, a.APNT_YMD
from APPOINTMENT a
join PATIENT p
on a.pt_no = p.pt_no
join doctor d
on a.MDDR_ID = d.DR_ID
where a.APNT_YMD like '2022-04-13%' and a.APNT_CNCL_YN = 'n' and a.MCDP_CD ='cs'
order by a.APNT_YMD
