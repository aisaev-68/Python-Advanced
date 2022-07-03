select st.full_name from students_groups sg, students st
where sg.group_id = st.group_id and sg.teacher_id =
(select teacher_id from
(select a.teacher_id, avg(ag.grade) as avg_grade from assignments a, assignments_grades ag
where a.assisgnment_id = ag.assisgnment_id
group by a.teacher_id
order by avg_grade desc limit 1));



select full_name from
(select s.full_name, teach.teacher_id from teachers teach
join students_groups sg on teach.teacher_id = sg.teacher_id
join students s on sg.group_id = s.group_id)
where teacher_id =
(select teacher_id from
(select a.teacher_id, avg(ag.grade) as avg_grade from assignments a
join assignments_grades ag on a.assisgnment_id = ag.assisgnment_id
group by a.teacher_id
order by avg_grade desc
limit 1));