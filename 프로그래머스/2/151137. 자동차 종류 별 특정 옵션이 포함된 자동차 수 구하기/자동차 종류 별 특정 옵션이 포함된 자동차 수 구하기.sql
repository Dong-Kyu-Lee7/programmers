-- 코드를 입력하세요
# SELECT *
select CAR_TYPE, count(car_id) cars
from CAR_RENTAL_COMPANY_CAR 
where instr(OPTIONS,'통풍시트')
    or instr(OPTIONS,'열선시트')
    or instr(OPTIONS,'가죽시트')
group by CAR_TYPE
order by CAR_TYPE