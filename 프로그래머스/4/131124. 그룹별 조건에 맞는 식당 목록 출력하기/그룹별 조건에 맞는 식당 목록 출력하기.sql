-- 코드를 입력하세요
SELECT p.MEMBER_NAME, r.REVIEW_TEXT, substr(r.REVIEW_DATE,1,10) REVIEW_DATE
from MEMBER_PROFILE p
join REST_REVIEW r
on p.MEMBER_ID = r.MEMBER_ID
where p.MEMBER_ID = (
    select MEMBER_ID
    from REST_REVIEW
    group by MEMBER_ID
    order by count(MEMBER_ID) desc
    limit 1
    )
order by r.REVIEW_DATE, r.REVIEW_TEXT
