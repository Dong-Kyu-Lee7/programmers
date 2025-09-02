-- 코드를 입력하세요
SELECT u.user_id, u.nickname, concat(u.city, ' ', u.STREET_ADDRESS1, ' ', u.STREET_ADDRESS2) 전체주소, concat_ws('-', substr(u.tlno,1,3), substr(u.tlno,4,4), substr(u.tlno,8,4)) 전화번호
from USED_GOODS_BOARD b
join USED_GOODS_USER u
on b.WRITER_ID = USER_ID
group by b.WRITER_ID
having count(b.WRITER_ID) >= 3
order by u.user_id desc