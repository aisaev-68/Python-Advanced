select a.full_name as 'Customer full name',
a.city as "City customer",
m.full_name as 'Manager full name',
m.city as "City mager",
o.purchase_amount as 'Purchase amount',
o.date as 'Date' from "customer" a
join "manager" m on m.manager_id = a.manager_id
join "order" o on a.customer_id = o.customer_id
where a.city != m.city