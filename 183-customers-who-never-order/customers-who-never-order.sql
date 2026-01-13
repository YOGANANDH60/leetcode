# Write your MySQL query statement below

SELECT name AS Customers 
FROM Customers AS T1
LEFT JOIN Orders AS T2
  ON T1.ID = T2.customerID
WHERE T2.ID IS NULL;

