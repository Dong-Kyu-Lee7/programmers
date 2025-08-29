-- 코드를 입력하세요
# SELECT *
select i.animal_id, i.name
from ANIMAL_INS i
join ANIMAL_OUTS o
on i.animal_id = o.animal_id
where i.datetime > o.datetime
# group by i.ANIMAL_ID
order by i.datetime