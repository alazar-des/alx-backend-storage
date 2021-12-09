-- create procedure
-- Insert row to a correction table
DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id int, IN project_name varchar(255), IN score int)
BEGIN
	DECLARE proj_id int;
	-- select id and copy to project id
	SELECT id INTO proj_id FROM projects WHERE name=project_name;

	-- if project name doesn't exist insert to projects
	IF (proj_id IS NULL)
	THEN
		-- insert project name to projects
		INSERT INTO projects (name) VALUES (project_name);
		-- retrive id
		SELECT id INTO proj_id FROM projects WHERE name=project_name;
	END IF;

	-- insert correction
       	INSERT INTO corrections (user_id, project_id, score)
       	VALUES (user_id, proj_id, score);
END; //

DELIMITER ;
