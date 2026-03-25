-- 코드를 입력하세요
SELECT
    u1.title,
    u1.board_id,
    u2.reply_id,
    u2.WRITER_ID,
    u2.CONTENTS,
    substr(u2.CREATED_DATE,1,10) CREATED_DATE
from USED_GOODS_BOARD u1
join USED_GOODS_REPLY u2
on u1.board_id = u2.BOARD_ID
# where u1.CREATED_DATE like '2022-10-%'
where u1.created_date >= '2022-10-01' and u1.created_date < '2022-11-01'
order by u2.CREATED_DATE, u1.TITLE