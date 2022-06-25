select distinct b.maker from
(select model, speed from pc) as a
join product b on a.model = b.model
where a.speed >= 450