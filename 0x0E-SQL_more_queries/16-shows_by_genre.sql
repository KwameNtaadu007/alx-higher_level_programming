-- Script lists all shows, and all genres linked to the show, from the database hbtn_0d_tvshows.
-- If a show has no genre, display NULL in the genre column
-- Each record displays: tv_shows.title - tv_genres.name
-- Results are sorted in ascending order using the show title and genre name
-- Just 1 SELECT statement is allowed
-- mysql is passed as database name as argument of mysql command

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
