/*
Task:
Write a script that displays the top 3 cities' temperatures during July and August ordered by temperature (descending).
*/

-- Select top 3 cities' temperatures during July and August, ordered by temperature (descending)
SELECT city, temperature
FROM hbtn_0c_0.temperature_data
WHERE MONTH(date) IN (7, 8)  -- Filter for July and August
ORDER BY temperature DESC
LIMIT 3;  -- Limit to top 3 results

