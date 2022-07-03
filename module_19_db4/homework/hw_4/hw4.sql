-- max select
select sg.group_id, count(*) as count_gr from students_groups sg, assignments a, assignments_grades ag
where a.teacher_id = sg.teacher_id
and a.assisgnment_id = ag.assisgnment_id
and CAST(strftime('%s', a.due_date)  AS  integer) < CAST(strftime('%s', ag.date)  AS  integer)
group by sg.group_id
order by count_gr desc limit 1;

-- min select
select sg.group_id, count(*) as count_gr from students_groups sg, assignments a, assignments_grades ag
where a.teacher_id = sg.teacher_id
and a.assisgnment_id = ag.assisgnment_id
and CAST(strftime('%s', a.due_date)  AS  integer) < CAST(strftime('%s', ag.date)  AS  integer)
group by sg.group_id
order by count_gr asc limit 1;


-- avg select
select avg(count_gr) from
(select sg.group_id, count(*) as count_gr from students_groups sg, assignments a, assignments_grades ag
where a.teacher_id = sg.teacher_id
and a.assisgnment_id = ag.assisgnment_id
and CAST(strftime('%s', a.due_date)  AS  integer) < CAST(strftime('%s', ag.date)  AS  integer)
group by sg.group_id);



-- JOIN
-- max
select sg.group_id, count(*) as count_gr from students_groups sg
join assignments a on sg.teacher_id = a.teacher_id
join assignments_grades ag on a.assisgnment_id = ag.assisgnment_id
where CAST(strftime('%s', a.due_date)  AS  integer) < CAST(strftime('%s', ag.date)  AS  integer)
group by sg.group_id
order by count_gr desc limit 1;

-- min
select sg.group_id, count(*) as count_gr from students_groups sg
join assignments a on sg.teacher_id = a.teacher_id
join assignments_grades ag on a.assisgnment_id = ag.assisgnment_id
where CAST(strftime('%s', a.due_date)  AS  integer) < CAST(strftime('%s', ag.date)  AS  integer)
group by sg.group_id
order by count_gr asc limit 1;

-- avg
select avg(count_gr) from
(select sg.group_id, count(*) as count_gr from students_groups sg
join assignments a on sg.teacher_id = a.teacher_id
join assignments_grades ag on a.assisgnment_id = ag.assisgnment_id
where CAST(strftime('%s', a.due_date)  AS  integer) < CAST(strftime('%s', ag.date)  AS  integer)
group by sg.group_id);