-- 코드를 작성해주세요
select e.emp_no, e.EMP_NAME,
    case
        when avg(g.score) >= 96 then 'S'
        when avg(g.score) >= 90 then 'A'
        when avg(g.score) >= 80 then 'B'
        else 'C'
    end grade,
    
    case
        when avg(g.score) >= 96 then e.sal * 0.2
        when avg(g.score) >= 90 then e.sal * 0.15
        when avg(g.score) >= 80 then e.sal * 0.1
        else e.sal * 0    
    end bonus
from HR_EMPLOYEES e
join HR_GRADE g
on e.emp_no = g.emp_no
group by e.emp_no
order by e.emp_no