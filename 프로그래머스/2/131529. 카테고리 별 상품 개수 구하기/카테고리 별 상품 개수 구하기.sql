-- 코드를 입력하세요
SELECT substr(PRODUCT_CODE,1,2) category, count(PRODUCT_ID) products
# select *
from product
group by substr(PRODUCT_CODE,1,2)
order by PRODUCT_CODE asc