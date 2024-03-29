--This will list all shows contained in hbtn_0d_tvshows without a genre linked
-- This aalso lists all rows of a database that don't have one column
SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id;
