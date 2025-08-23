-- 코드를 작성해주세요
select sum(g.score) score, e.EMP_NO, e.EMP_NAME, e.POSITION, e.email
from HR_EMPLOYEES e
join HR_GRADE g
on e.emp_no = g.emp_no
group by g.emp_no
order by score desc
limit 1