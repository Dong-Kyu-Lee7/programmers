-- 코드를 입력하세요
SELECT CAR_ID, round(avg(timestampdiff(day, start_Date, end_date)+1),1) AVERAGE_DURATION
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID
having AVERAGE_DURATION >= 7
order by AVERAGE_DURATION desc, CAR_ID desc