/*
Task:
Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
*/

-- Calculate average temperature in Fahrenheit by city and order by temperature (descending)
SELECT city, AVG((temperature * 9/5) + 32) AS average_temperature_fahrenheit
FROM hbtn_0c_0.temperature_data
GROUP BY city
ORDER BY average_temperature_fahrenheit DESC;

