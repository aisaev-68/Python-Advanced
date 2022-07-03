select a.assisgnment_id, a.assignment_text, avg(ag.grade) from assignments a
join assignments_grades ag on a.assisgnment_id = ag.assisgnment_id
where a.assignment_text like '%прочит%' or a.assignment_text like 'выуч%'
group by a.assisgnment_id
order by a.assisgnment_id;