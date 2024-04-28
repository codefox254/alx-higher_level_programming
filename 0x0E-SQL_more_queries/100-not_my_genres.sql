-- SQL script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT name
FROM tv_genres
WHERE name NOT IN
(SELECT g.name
FROM tv_genres g
LEFT JOIN tv_show_genres sg ON g.id = sg.genre_id
LEFT JOIN tv_shows s ON sg.show_id = s.id
WHERE s.title = 'Dexter')
GROUP BY name
ORDER BY name ASC;
