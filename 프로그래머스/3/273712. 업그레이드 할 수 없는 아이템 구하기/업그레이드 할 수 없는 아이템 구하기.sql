-- 코드를 작성해주세요
# select *
select i.ITEM_ID, i.ITEM_name, i.rarity
from ITEM_INFO i
left join ITEM_TREE t
on i.item_id = t.PARENT_ITEM_ID
where t.PARENT_ITEM_ID is null
order by i.item_id desc
