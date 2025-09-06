-- 코드를 입력하세요
SELECT month(start_date) month, CAR_ID, count(*) records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where month(start_date) between 8 and 10
    and (car_id in (
            select car_id
            from CAR_RENTAL_COMPANY_RENTAL_HISTORY
            where START_DATE between '2022-08-01' and '2022-10-31'
            group by car_id
            having count(car_id) >= 5
        ))
group by month, CAR_ID
order by month, car_id desc