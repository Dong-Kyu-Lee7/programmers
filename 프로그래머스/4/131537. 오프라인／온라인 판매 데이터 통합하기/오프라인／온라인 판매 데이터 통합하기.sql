-- 코드를 입력하세요
SELECT substr(sales_date,1,10) SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
from ONLINE_SALE
where substr(sales_date,1,7) = '2022-03'

union

select substr(sales_date,1,10) SALES_DATE, PRODUCT_ID, null USER_ID, SALES_AMOUNT
from OffLINE_SALE
where substr(sales_date,1,7) = '2022-03'

order by SALES_DATE, PRODUCT_ID, USER_ID