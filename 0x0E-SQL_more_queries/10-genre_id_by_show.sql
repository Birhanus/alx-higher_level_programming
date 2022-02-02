-- sql script that list all show in hbtn_0d_tvshows that have at least on genre linked
-- Records are sorted by ascending tv_show.title and tv_show_genres.genre_id

SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
        INNER JOIN `tv_show_genres` AS g
	ON s.`id` = g.`show_id`
ORDER BY s.`title`, g.`genre_id`;