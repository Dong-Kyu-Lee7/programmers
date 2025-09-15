-- 코드를 입력하세요
SELECT fh.FLAVOR
from FIRST_HALF fh
join (
    select flavor, sum(TOTAL_ORDER) TOTAL_ORDER
    from july
    group by flavor
) j
on fh.flavor = j.flavor
order by fh.TOTAL_ORDER + j.TOTAL_ORDER desc
limit 3
