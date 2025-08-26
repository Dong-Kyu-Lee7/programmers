-- 코드를 작성해주세요
select a.id, a.genotype, b.GENOTYPE PARENT_GENOTYPE
from ECOLI_DATA a
join ecoli_data b
on a.parent_id = b.id
where (a.GENOTYPE & b.GENOTYPE) = b.GENOTYPE
order by a.id 