-- 코드를 입력하세요
SELECT i.rest_id, i.rest_name, i.food_type, i.favorites, i.address, round(avg(r.review_score),2) SCORE
from REST_INFO i
join REST_REVIEW r
on i.REST_ID = r.REST_ID
where i.address like '서울%'
group by i.rest_id
order by SCORE desc, i.favorites desc