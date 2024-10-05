-- Write query to find the number of grade A's given by the teacher who has graded the most assignments

-- groups by teacher_id and counts the number of assignments graded by each teacher
WITH TeacherGradingCounts AS (
    SELECT teacher_id, COUNT(*) AS total_graded
    FROM assignments
    WHERE grade IS NOT NULL
    GROUP BY teacher_id
)


-- selects the teacher_id of the teacher who has graded the most assignments
, MostGradingTeacher AS (
    SELECT teacher_id
    FROM TeacherGradingCounts
    ORDER BY total_graded DESC
    LIMIT 1
)

-- counts grade A
SELECT COUNT(*) AS grade_a_count
FROM assignments
WHERE teacher_id = (SELECT teacher_id FROM MostGradingTeacher)
  AND grade = 'A';
