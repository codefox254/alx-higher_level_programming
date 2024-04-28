-- SQL script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT title
FROM tv_shows
WHERE title NOT IN
(SELECT s.title
FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
LEFT JOIN tv_genres g ON sg.genre_id = g.id
WHERE g.name = 'Comedy')
GROUP BY title
ORDER BY title ASC;
