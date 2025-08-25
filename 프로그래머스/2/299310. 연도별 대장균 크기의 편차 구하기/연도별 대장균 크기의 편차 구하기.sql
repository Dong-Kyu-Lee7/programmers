-- 코드를 작성해주세요
select year(DIFFERENTIATION_DATE) YEAR,
    (select max(SIZE_OF_COLONY)
    from ECOLI_DATA
    where YEAR = YEAR(DIFFERENTIATION_DATE)) - SIZE_OF_COLONY YEAR_DEV,
    id
from ECOLI_DATA 
order by year, year_dev