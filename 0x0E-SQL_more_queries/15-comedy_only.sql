-- Script lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table has just 1 record where name = Comedy (However id may be different)
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order using the show title
-- Just 1 SELECT statement is allowed
-- mysql database name is passed as argument of mysql command

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
