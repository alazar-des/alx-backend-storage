-- create procedure
-- save wighted average into row
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(userId int)
BEGIN
	DECLARE tot_score float;
	DECLARE tot_weight int;
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
END; //

DELIMITER ;
