-- 코드를 작성해주세요
select id,
    case
        when ed.per <= 0.25 then 'CRITICAL'
        when ed.per <= 0.5 then 'HIGH'
        when ed.per <= 0.75 then 'MEDIUM'
        else 'LOW'
    end colony_name
from (
    select id, percent_rank() over (order by SIZE_OF_COLONY desc) per
    from ECOLI_DATA) ed
order by id