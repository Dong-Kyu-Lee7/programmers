-- 코드를 입력하세요
SELECT concat('/home/grep/src/', f.BOARD_ID, '/', f.FILE_ID, f.FILE_NAME, f.FILE_EXT) FILE_PATH
from USED_GOODS_BOARD b
left join USED_GOODS_FILE f
on b.BOARD_ID = f.BOARD_ID
where views = (
    select max(views)
    from USED_GOODS_BOARD
    )
order by f.FILE_ID desc
# limit 1