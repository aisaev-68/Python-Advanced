select a.full_name as 'Customer full name', o.order_no
from customer a
join "order" o on a.customer_id = o.customer_id
where o.manager_id is null