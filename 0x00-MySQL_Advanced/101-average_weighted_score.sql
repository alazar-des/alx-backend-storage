-- create procedure
-- save wighted average into row
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN

	DECLARE tot_score float;
	DECLARE tot_weight int;
	DECLARE userId int;
	DECLARE n int;
	DECLARE i int;
	-- count all users
	SELECT COUNT(*) FROM users INTO n;
	SET i=0;

	-- loop through all users
	WHILE i<n DO
	      -- set user id
	      SELECT id INTO userId FROM users LIMIT i,1;
	      -- calculate average
	      SELECT SUM(c.score * p.weight), SUM(p.weight)
	      INTO tot_score, tot_weight
	      FROM corrections c, projects p
	      WHERE c.user_id = userId
	        AND c.project_id = p.id;

	      -- update average score
	      UPDATE users
	      SET average_score = tot_score / tot_weight
	      WHERE id = userId;
	      -- increament
	      SET i=i+1;
	END WHILE;
END; //

DELIMITER ;
