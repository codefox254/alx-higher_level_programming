/*
Task:
Write a script that displays the max temperature of each state (ordered by State name).
*/

-- Select max temperature of each state, ordered by State name
SELECT State, MAX(temperature) AS max_temperature
FROM hbtn_0c_0.temperature_data
GROUP BY State
ORDER BY State;

