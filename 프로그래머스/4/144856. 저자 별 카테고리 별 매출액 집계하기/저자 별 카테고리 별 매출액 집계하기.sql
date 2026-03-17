-- 코드를 입력하세요
SELECT a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, sum(bs.sales * b.price) TOTAL_SALES
from BOOK b
join AUTHOR a
on b.AUTHOR_ID = a.AUTHOR_ID
join BOOK_SALES bs
on b.BOOK_ID = bs.BOOK_ID
# where bs.sales_date like '2022-01%'
where bs.sales_date >= '2022-01-01' and bs.sales_date < '2022-02-01'
group by a.AUTHOR_ID, b.CATEGORY
# having sum(bs.sales) * b.price
order by a.AUTHOR_ID, b.CATEGORY desc