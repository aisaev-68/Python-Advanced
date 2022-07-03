select full_name, avg(grade) as avg_grade from students
join assignments_grades ag on students.student_id = ag.student_id
group by full_name
order by avg_grade desc limit 10


select st.full_name, avg(asg.grade) as avg_grade from students st, assignments_grades asg
where st.student_id = asg.student_id
group by st.full_name
order by avg_grade desc
limit 10