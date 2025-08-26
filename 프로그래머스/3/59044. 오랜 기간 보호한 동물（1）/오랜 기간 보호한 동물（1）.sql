-- 코드를 입력하세요
SELECT i.name name, i.DATETIME DATETIME
from animal_ins i
left join animal_outs o
on i.animal_id = o.animal_id
where o.datetime is null
order by i.DATETIME
limit 3