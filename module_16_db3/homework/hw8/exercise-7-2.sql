select a.model, a.price
from (select model, price from pc
union
select model, price from laptop
union
select model, price from printer) as a
join product p on a.model = p.model
where p.maker = 'B'