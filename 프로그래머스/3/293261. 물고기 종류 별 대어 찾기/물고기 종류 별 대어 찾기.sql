-- 코드를 작성해주세요
select i.ID, n.fish_name, i.length
from FISH_INFO i
join FISH_NAME_INFO n
on i.FISH_TYPE = n.FISH_TYPE
where (i.fish_type, i.length) in (
    select fish_type, max(length)
    from FISH_INFO 
    group by fish_type)
order by i.id