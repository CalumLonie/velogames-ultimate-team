-- This is the SQL file which holds all the tables and procedures used in the Velogames
-- Ultimate Team project. It also contains any global variables to be set. 

SET GLOBAL local_infile = 1;

-- The list of input and output tables. 
CREATE TABLE input (
names TEXT,
cost INTEGER,
points INTEGER
);
CREATE TABLE input_ar (
names TEXT,
cost INTEGER,
points INTEGER
);
CREATE TABLE input_c (
names TEXT,
cost INTEGER,
points INTEGER
);
CREATE TABLE input_s (
names TEXT,
cost INTEGER,
points INTEGER
);
CREATE TABLE input_u (
names TEXT,
cost INTEGER,
points INTEGER
);

CREATE TABLE output (
names TEXT,
cost INTEGER,
points INTEGER
);
CREATE TABLE output_ar (
names TEXT,
cost INTEGER,
points INTEGER
);
CREATE TABLE output_c (
names TEXT,
cost INTEGER,
points INTEGER
);
CREATE TABLE output_s (
names TEXT,
cost INTEGER,
points INTEGER
);
CREATE TABLE output_u (
names TEXT,
cost INTEGER,
points INTEGER
);
CREATE TABLE output_w (
names TEXT,
cost INTEGER,
points INTEGER
);
CREATE TABLE output_inter (
names TEXT,
cost INTEGER,
points INTEGER
);

-- This shows the declaration of all the procedures needed. 
DELIMITER \\
CREATE PROCEDURE filtering (IN max_cost INTEGER, IN num INTEGER)
BEGIN
DECLARE counter INT;
SET counter = max_cost;
WHILE counter >= 4 DO
	INSERT INTO output
    SELECT * FROM input
    WHERE cost = counter
    ORDER BY points DESC
    LIMIT num;
    SET counter = counter - 2;
END WHILE;
END\\

CREATE PROCEDURE filtering_ar (IN max_cost INTEGER)
BEGIN
DECLARE counter INT;
SET counter = max_cost;
WHILE counter >= 4 DO
	INSERT INTO output_ar
    SELECT * FROM input_ar
    WHERE cost = counter
    ORDER BY points DESC
    LIMIT 3;
    SET counter = counter - 2;
END WHILE;
END\\

CREATE PROCEDURE filtering_c (IN max_cost INTEGER)
BEGIN
DECLARE counter INT;
SET counter = max_cost;
WHILE counter >= 4 DO
	INSERT INTO output_c
    SELECT * FROM input_c
    WHERE cost = counter
    ORDER BY points DESC
    LIMIT 3;
    SET counter = counter - 2;
END WHILE;
END\\

CREATE PROCEDURE filtering_s (IN max_cost INTEGER)
BEGIN
DECLARE counter INT;
SET counter = max_cost;
WHILE counter >= 4 DO
	INSERT INTO output_s
    SELECT * FROM input_s
    WHERE cost = counter
    ORDER BY points DESC
    LIMIT 2;
    SET counter = counter - 2;
END WHILE;
END\\

CREATE PROCEDURE filtering_u (IN max_cost INTEGER)
BEGIN
DECLARE counter INT;
SET counter = max_cost;
WHILE counter >= 4 DO
	INSERT INTO output_u
    SELECT * FROM input_u
    WHERE cost = counter
    ORDER BY points DESC
    LIMIT 4;
    SET counter = counter - 2;
END WHILE;
END\\
DELIMITER ;