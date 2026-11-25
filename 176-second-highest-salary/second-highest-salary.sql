# Write your MySQL query statement below
select(
    select salary
from (
    select 
    id, 
    salary, 
    dense_rank() over (order by salary desc) as ra
     from
    Employee) as temp
where ra = 2
LIMIT 1
) as SecondHighestSalary;