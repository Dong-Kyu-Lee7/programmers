-- 코드를 작성해주세요
select i.ITEM_ID, i.ITEM_NAME, i.RARITY
from item_info i
left join ITEM_TREE t
on i.ITEM_ID = t.ITEM_ID
where t.PARENT_ITEM_ID in (
    select item_id
    from item_info
    where rarity = 'rare'
)
order by i.item_id desc