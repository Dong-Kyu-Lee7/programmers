-- 코드를 입력하세요
SELECT p.product_id, p.product_name, sum(o.amount * p.price) TOTAL_SALES
from FOOD_PRODUCT p
join FOOD_ORDER o
on p.PRODUCT_ID = o.PRODUCT_ID
where year(o.PRODUCE_DATE) = 2022 and month(o.PRODUCE_DATE) = 5
group by p.product_id
order by TOTAL_SALES desc, p.product_id