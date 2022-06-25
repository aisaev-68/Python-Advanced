select a.full_name as 'Customer full name', count(*)
from customer a
join manager m on m.manager_id = a.manager_id
join "order" o on a.customer_id = o.customer_id
group by a.full_name