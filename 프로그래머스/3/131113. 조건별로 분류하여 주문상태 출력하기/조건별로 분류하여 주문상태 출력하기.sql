-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, substr(OUT_DATE,1,10) OUT_DATE,
    case
        when timestampdiff(day, '2022-05-01', OUT_DATE) >=1 then '출고대기'
        when out_date is null then '출고미정'
        else '출고완료'
    end 출고여부
from food_order
# where substr(out_date,1,10) = '2022-05-01'

order by order_id