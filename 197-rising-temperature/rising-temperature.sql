# Write your MySQL query statement below
WITH Comparedtemp AS (
    SELECT 
        id,
        recordDate,
        temperature,
        LAG(temperature) OVER (ORDER BY recordDate) AS pretemp,
        LAG(recordDate) OVER (ORDER BY recordDate) AS predate
    FROM Weather
)
SELECT id
FROM Comparedtemp
WHERE temperature > pretemp
and datediff(recordDate,predate) = 1;