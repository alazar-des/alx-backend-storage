-- create procedure
-- save average into row
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(userId int)
BEGIN
	DECLARE avg_score float;
	-- calculate average
	SELECT AVG(score) INTO avg_score
	FROM corrections
	WHERE user_id = userId;

	-- update average score
	UPDATE users
	SET average_score = avg_score
	WHERE id = userId;
END; //

DELIMITER ;
