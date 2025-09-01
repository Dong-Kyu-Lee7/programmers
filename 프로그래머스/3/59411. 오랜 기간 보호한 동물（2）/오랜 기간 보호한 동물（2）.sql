-- 코드를 입력하세요
# SELECT *
select i.ANIMAL_ID, i.name
from ANIMAL_INS i
join ANIMAL_OUTS o
on i.ANIMAL_ID = o.ANIMAL_ID
order by timestampdiff(day, i.DATETIME, o.DATETIME) desc
limit 2