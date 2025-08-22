-- 코드를 입력하세요
# select *,
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE,
    case
        when status = 'sale' then '판매중'
        when status = 'reserved' then '예약중'
        else '거래완료'        
        
    end status
from USED_GOODS_BOARD 
where instr(CREATED_DATE, '2022-10-05')
order by BOARD_ID desc