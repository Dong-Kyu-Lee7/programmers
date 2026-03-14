-- 코드를 작성해주세요
# select *
select count(i.id) fish_count
from fish_info i
join fish_name_info ni
on i.fish_type = ni.fish_type
where ni.fish_name in ('bass','snapper')
order by fish_count