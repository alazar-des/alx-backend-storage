-- function
-- safe divide fucntion
DELIMITER //

CREATE FUNCTION SafeDiv (a int, b int)
RETURNS float

BEGIN
	IF (b = 0)
	THEN
		RETURN 0;
	END IF;

	RETURN a / b;
END; //

DELIMITER ;
