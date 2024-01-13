# Write your MySQL query statement below
SELECT
    ud.unique_id, u.name
FROM 
    Employees u
LEFT JOIN 
    EmployeeUNI ud ON u.id = ud.id;