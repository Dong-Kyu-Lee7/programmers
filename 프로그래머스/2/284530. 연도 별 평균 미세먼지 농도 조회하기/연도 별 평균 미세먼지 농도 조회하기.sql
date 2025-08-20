-- 코드를 작성해주세요
# select *
select year(ym) year, round(avg(PM_VAL1),2) PM10, round(avg(PM_VAL2),2) 'PM2.5'
FROM AIR_POLLUTION
WHERE LOCATION2 = '수원'
GROUP BY year(ym)
order by year(ym)