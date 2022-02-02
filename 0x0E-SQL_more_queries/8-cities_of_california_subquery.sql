-- sql script that lists all the cities of California that be found
-- in the database hbtn_0d-usa.
-- That states table contains only record where name = california (but the id can
-- be different.
-- Results must be sorted in ascending order by cities.id
-- Your are nor allowed to use the JOIN keyword
-- The database name will be passed as an argument of the mysql command

SELECT `id`, `name` FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
 
