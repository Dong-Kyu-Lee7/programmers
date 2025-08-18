-- 코드를 입력하세요
# SELECT *
select i.INGREDIENT_TYPE INGREDIENT_TYPE, sum(h.total_order) total_order
from FIRST_HALF h
join ICECREAM_INFO i
on h.flavor = i.flavor
group by i.ingredient_type
