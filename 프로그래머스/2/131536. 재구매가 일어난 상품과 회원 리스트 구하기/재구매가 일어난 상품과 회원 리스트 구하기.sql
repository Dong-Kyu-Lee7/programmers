-- 코드를 입력하세요
SELECT user_id, product_id
from ONLINE_SALE 
group by USER_ID, PRODUCT_ID
having count(user_id) >= 2
order by USER_ID, PRODUCT_ID desc