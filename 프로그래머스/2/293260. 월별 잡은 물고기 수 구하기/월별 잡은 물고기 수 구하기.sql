-- 코드를 작성해주세요
# select *
select count(id) fish_count, month(time) month
from fish_info
# where length is not null
group by month
order by month(time)