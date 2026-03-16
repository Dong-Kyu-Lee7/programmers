-- 코드를 입력하세요
SELECT USER_ID, product_id
from ONLINE_SALE 
group by USER_ID, PRODUCT_ID
having count(user_id) >= 2
order by USER_ID asc, PRODUCT_ID desc