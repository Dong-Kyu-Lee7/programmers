-- 코드를 입력하세요
SELECT cart_id
from CART_PRODUCTS
where NAME in ('yogurt', 'milk')
group by cart_id
having count(distinct(NAME)) = 2
# order by cart_id