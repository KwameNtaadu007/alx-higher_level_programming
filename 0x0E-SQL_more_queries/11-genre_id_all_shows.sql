-- Script lists all shows in the database hbtn_0d_tvshows.
-- Each record displays:
-- tv_shows.title - tv_show_genres.genre_id
-- Results are sorted in ascending order using tv_shows.title and tv_show_genres.genre_id
-- Display NULL if a show does not have a genre 
-- Just 1  SELECT statement is allowed
-- mysql is passed as database name as argument of mysql command

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
