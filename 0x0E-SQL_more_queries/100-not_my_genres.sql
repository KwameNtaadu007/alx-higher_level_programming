-- Script which lists all genres not linked to the Dexter show
-- The tv_shows table has just 1 record where title = Dexter (However the id may be different)
-- Each record displays: tv_genres.name
-- Results are sorted in ascending order using the genre name
-- maximum of 2 SELECT statement are allowed
-- mysql is passed as database name as argument of mysql command

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN
(SELECT tv_genres.id
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter")
ORDER BY tv_genres.name;
