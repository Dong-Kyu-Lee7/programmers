-- 코드를 입력하세요
# SELECT *
select MEMBER_ID, MEMBER_NAME, GENDER, substr(DATE_OF_BIRTH,1,10) DATE_OF_BIRTH
from member_profile
where instr(DATE_OF_BIRTH, '-03-') and tlno is not null and gender = 'W'
order by MEMBER_ID