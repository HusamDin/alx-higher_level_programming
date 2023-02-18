-- This script uses the hbtn_0d_tvshows database
-- to list all genres of the show Dexter
SELECT `name`
FROM `tv_genres`
JOIN `tv_show_genres`
ON `id` = `genre_id`
WHERE `show_id` =
      (
      SELECT `id` FROM `tv_shows`
      WHERE `title` = 'Dexter'
      );
