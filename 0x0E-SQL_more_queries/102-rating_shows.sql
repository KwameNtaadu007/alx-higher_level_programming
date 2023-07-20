-- Script lists all shows in hbtn_0d_tvshows_rate using their rating.
-- Each record displays: tv_shows.title - rating sum
-- Results are sorted in acending order using the rating
-- mysql is passed as  database name as argument of mysql command

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
INNER JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;
