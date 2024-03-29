-- Script lists all shows in hbtn_0d_tvshows without a genre linked.
-- Each record displays:
-- tv_shows.title - tv_show_genres.genre_id
-- Results are sorted in ascending order using tv_shows.title and tv_show_genres.genre_id
-- Just 1 SELECT statement is allowed
-- mysql is passed as database name as argument of mysql command

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;

