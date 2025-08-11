-- 코드를 입력하세요
SELECT HISTORY_ID,
    CAR_ID,
    substr(START_DATE,1,10) START_DATE,
    substr(end_DATE,1,10) END_DATE,
    if(timestampdiff(day, START_DATE, END_DATE)+1 >= 30, '장기 대여', '단기 대여') RENT_TYPE
# select *
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where START_DATE like '2022-09-%'
order by HISTORY_ID desc