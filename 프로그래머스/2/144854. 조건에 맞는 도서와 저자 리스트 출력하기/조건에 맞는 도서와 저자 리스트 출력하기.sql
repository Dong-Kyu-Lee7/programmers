-- 코드를 입력하세요
# SELECT *
select b.BOOK_ID, a.AUTHOR_NAME, substr(b.PUBLISHED_DATE,1,10) PUBLISHED_DATE
from book b
join author a
on b.AUTHOR_ID = a.AUTHOR_ID
where b.category = '경제'
# group by b.category
order by b.PUBLISHED_DATE