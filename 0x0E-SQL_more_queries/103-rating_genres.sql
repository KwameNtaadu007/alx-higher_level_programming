-- Script lists all genres in the database hbtn_0d_tvshows_rate using their rating.
-- Each record displays: tv_genres.name - rating sum
-- Results are sorted in ascending order using their rating
-- mysql is passed as database name as argument of mysql command

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings
ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.id
ORDER BY rating DESC;
