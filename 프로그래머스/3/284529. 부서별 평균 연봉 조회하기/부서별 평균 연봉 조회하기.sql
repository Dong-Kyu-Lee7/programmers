-- 코드를 작성해주세요
# select *
select e.dept_id, d.DEPT_NAME_EN, round(avg(e.sal)) AVG_SAL
from HR_DEPARTMENT d
join HR_EMPLOYEES e
on d.DEPT_ID = e.DEPT_ID
group by e.DEPT_ID
order by AVG_SAL desc