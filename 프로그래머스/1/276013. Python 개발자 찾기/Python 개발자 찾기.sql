-- 코드를 작성해주세요
select id, email, first_name, last_name
from developer_infos
where instr(SKILL_1, 'Python') or instr(SKILL_2, 'Python') or instr(SKILL_3, 'Python')
order by id