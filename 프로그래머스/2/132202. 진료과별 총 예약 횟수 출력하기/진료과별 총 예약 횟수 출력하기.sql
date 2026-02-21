-- 코드를 입력하세요
SELECT MCDP_CD 진료과코드, count(APNT_YMD) 5월예약건수
# select *
from APPOINTMENT
where instr(APNT_YMD,'2022-05')
group by MCDP_CD
order by 5월예약건수 asc, MCDP_CD asc