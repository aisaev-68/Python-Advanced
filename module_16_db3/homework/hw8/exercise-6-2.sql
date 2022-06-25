select distinct product.maker, laptop.speed
FROM product JOIN
laptop ON product.model = laptop.model
WHERE laptop.hd >= 10