-- 코드를 입력하세요
SELECT distinct r.car_id
from CAR_RENTAL_COMPANY_CAR c
join CAR_RENTAL_COMPANY_RENTAL_HISTORY r
on c.car_id = r.car_id
where month(start_date) = 10 and c.car_type = '세단'
order by r.car_id desc