-- 코드를 작성해주세요
# select 
#     case
#         when month(DIFFERENTIATION_DATE) <= 3 then '1Q'
#         when month(DIFFERENTIATION_DATE) <= 6 then '2Q'
#         when month(DIFFERENTIATION_DATE) <= 9 then '3Q'
#         else '4Q'
#     end as QUARTER,
#     count(id) ECOLI_COUNT
# from ECOLI_DATA 
# group by QUARTER
# order by QUARTER

SELECT 
    CASE
        WHEN MONTH(DIFFERENTIATION_DATE) <= 3 THEN '1Q'
        WHEN MONTH(DIFFERENTIATION_DATE) <= 6 THEN '2Q'
        WHEN MONTH(DIFFERENTIATION_DATE) <= 9 THEN '3Q'
        ELSE '4Q'
    END AS QUARTER,
    COUNT(ID) AS ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY 
    CASE
        WHEN MONTH(DIFFERENTIATION_DATE) <= 3 THEN '1Q'
        WHEN MONTH(DIFFERENTIATION_DATE) <= 6 THEN '2Q'
        WHEN MONTH(DIFFERENTIATION_DATE) <= 9 THEN '3Q'
        ELSE '4Q'
    END
ORDER BY QUARTER;