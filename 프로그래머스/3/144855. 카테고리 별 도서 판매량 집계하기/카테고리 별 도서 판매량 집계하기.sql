-- 코드를 입력하세요
# SELECT *
select b.category, sum(bs.sales) total_sales
from BOOK b
join book_sales bs
on b.book_id = bs.book_id
where year(bs.sales_date) = 2022 and month(bs.sales_date) = 1
group by b.category
# having substr(bs.sales_date, 1,7) = '2022-01'

order by category