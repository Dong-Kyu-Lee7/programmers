-- 코드를 작성해주세요
select count(f2.FISH_TYPE) FISH_COUNT, f2.fish_name FISH_NAME
from fish_info f1
join fish_name_info f2
on f1.fish_type = f2.fish_type
group by f2.fish_name
order by FISH_COUNT desc