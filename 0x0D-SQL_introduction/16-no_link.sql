-- Select records with non-null name value from second_table, displaying score and name, ordered by score (descending)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
