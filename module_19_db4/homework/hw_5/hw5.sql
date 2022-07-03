-- count students for group
select table_group.group_id, count(*) as count_students from
(select sg.group_id from teachers t, students_groups sg
where sg.teacher_id = t.teacher_id) as table_group, students st
where st.group_id = table_group.group_id
group by table_group.group_id;

-- avg grade for groups
select s.group_id, avg(ag.grade) as avg_grade from teachers t
join students_groups sg on t.teacher_id = sg.teacher_id
join students s on sg.group_id = s.group_id
join assignments_grades ag on s.student_id = ag.student_id
group by sg.group_id
order by avg_grade asc;

-- due data
select sg.group_id, count(ag.grade) as count_gr from students_groups sg
join assignments a on sg.teacher_id = a.teacher_id
join assignments_grades ag on a.assisgnment_id = ag.assisgnment_id
where CAST(strftime('%s', a.due_date)  AS  integer) < CAST(strftime('%s', ag.date)  AS  integer)
group by sg.group_id
order by count_gr desc;

-- grade = 0
select sg.group_id, count(ag.grade) as count_gr from students_groups sg
join assignments a on sg.teacher_id = a.teacher_id
join assignments_grades ag on a.assisgnment_id = ag.assisgnment_id
where ag.grade = 0
group by sg.group_id
order by count_gr desc;

-- повторная сдача
select st.group_id, count(*) from students st,
(select ag.assisgnment_id, ag.student_id, count(*) as count from assignments_grades ag
group by ag.assisgnment_id, ag.student_id
having count(*) > 1
order by ag.assisgnment_id, ag.student_id) t,
(select group_id from teachers
join students_groups sg on teachers.teacher_id = sg.teacher_id) gr
where st.student_id = t.student_id
and st.group_id = gr.group_id
group by st.group_id;