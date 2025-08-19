-- 코드를 입력하세요
# SELECT *
select p.PRODUCT_CODE PRODUCT_CODE, sum(p.price * o.SALES_AMOUNT) SALES
from product p
join offline_sale o
on p.product_id = o.product_id
group by p.product_code
order by SALES desc, p.PRODUCT_CODE