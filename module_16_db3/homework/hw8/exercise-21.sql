select maker, max(price) from
(select model, price from pc) as a
join product b on a.model = b.model
group by b.maker