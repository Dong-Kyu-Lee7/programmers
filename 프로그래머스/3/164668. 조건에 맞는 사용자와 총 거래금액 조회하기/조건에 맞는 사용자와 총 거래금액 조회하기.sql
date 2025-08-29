-- 코드를 입력하세요
# SELECT *
select u.user_id, u.nickname, sum(b.price) total_price
from USED_GOODS_BOARD b
join USED_GOODS_USER u
on b.WRITER_ID = u.USER_ID
where b.STATUS = 'DONE'
group by b.writer_id
having sum(b.price) >= 700000
order by total_price