-- 코드를 입력하세요
# SELECT *
select truncate(price,-4) PRICE_GROUP, count(PRODUCT_ID) PRODUCTS
from product
group by PRICE_GROUP
order by PRICE_GROUP