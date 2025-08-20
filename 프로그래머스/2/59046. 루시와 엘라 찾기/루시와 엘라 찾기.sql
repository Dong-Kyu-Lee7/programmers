-- 코드를 입력하세요
SELECT ANIMAL_ID, name, SEX_UPON_INTAKE
from animal_ins
where NAME IN ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')
order by animal_id