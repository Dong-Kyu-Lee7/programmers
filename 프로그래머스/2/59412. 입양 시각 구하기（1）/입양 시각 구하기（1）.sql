-- 코드를 입력하세요
# SELECT *
select hour(DATETIME) HOUR, count(ANIMAL_ID) count
from ANIMAL_OUTS
where hour(DATETIME) >= 9 and hour(DATETIME) <= 19
group by hour(DATETIME)
order by hour(DATETIME)