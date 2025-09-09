-- 코드를 입력하세요
SELECT i.animal_id, i.animal_type, i.name
from ANIMAL_INS i
join ANIMAL_OUTS o
on i.animal_id = o.animal_id
where instr(i.SEX_UPON_INTAKE, 'intact') and
    (instr(o.SEX_UPON_OUTCOME, 'spayed') or instr(o.SEX_UPON_OUTCOME, 'Neutered'))
order by i.ANIMAL_ID