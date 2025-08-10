-- 코드를 작성해주세요
select count(FISH_TYPE) FISH_COUNT
from fish_info
where instr(TIME, '2021')
