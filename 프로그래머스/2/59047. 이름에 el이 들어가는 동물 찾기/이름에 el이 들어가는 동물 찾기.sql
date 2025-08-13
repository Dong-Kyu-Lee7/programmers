-- 코드를 입력하세요
SELECT ANIMAL_ID, name
from animal_ins
where instr(name, 'el') and animal_type = 'dog'
order by name