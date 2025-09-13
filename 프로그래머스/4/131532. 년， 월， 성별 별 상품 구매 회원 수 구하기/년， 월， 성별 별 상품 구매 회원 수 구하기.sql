-- 코드를 입력하세요
SELECT year(o.sales_Date) year, month(o.sales_Date) month, u.gender gender, count(distinct(u.user_id)) USERS
from USER_INFO u
join ONLINE_SALE o
on u.user_id = o.user_id
where u.gender is not null
group by year(o.sales_Date), month(o.sales_Date), u.gender
order by year(o.sales_Date), month(o.sales_Date), u.gender