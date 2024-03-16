-- Select max temperature of each state, ordered by State name
SELECT State, MAX(temperature) AS max_temperature
FROM temperatures
GROUP BY State
ORDER BY State;
