select t.full_name, avg(ag.grade) as avg_grade from teachers t
join assignments a on t.teacher_id = a.teacher_id
join assignments_grades ag on a.assisgnment_id = ag.assisgnment_id
group by a.teacher_id
order by avg_grade asc
limit 1;


select full_name, avg_grade from (
select teach.full_name, avg(ag.grade) as avg_grade
from teachers teach, assignments asg, assignments_grades ag
where teach.teacher_id = asg.teacher_id and asg.assisgnment_id = ag.assisgnment_id
group by teach.teacher_id order by avg_grade asc limit 1);