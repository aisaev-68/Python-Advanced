select a.full_name as 'Customer full name'
from "customer" a
left outer join "order" o on a.customer_id = o.customer_id
where date is null