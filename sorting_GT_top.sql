# This code is used to select the best scoring riders to determine the Top 100 teams in the
# Grand Tour contests.

# Clear the tables of old data. 
DELETE FROM input_ar;
DELETE FROM input_c;
DELETE FROM input_s;
DELETE FROM input_u;
DELETE FROM output_inter;
DELETE FROM output_ar;
DELETE FROM output_c;
DELETE FROM output_s;
DELETE FROM output_u;
DELETE FROM output_w;

# Load the data. 
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/France_AllRounder.csv'
INTO TABLE input_ar
FIELDS TERMINATED BY ',' ENCLOSED BY ''
LINES STARTING BY '' TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/France_Climber.csv'
INTO TABLE input_c
FIELDS TERMINATED BY ',' ENCLOSED BY ''
LINES STARTING BY '' TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/France_Sprinter.csv'
INTO TABLE input_s
FIELDS TERMINATED BY ',' ENCLOSED BY ''
LINES STARTING BY '' TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/France_Unclassified.csv'
INTO TABLE input_u
FIELDS TERMINATED BY ',' ENCLOSED BY ''
LINES STARTING BY '' TERMINATED BY '\n'
IGNORE 1 ROWS;

# Remove any rider who didn't score. 
DELETE FROM input_ar
WHERE points = 0;
DELETE FROM input_c
WHERE points = 0;
DELETE FROM input_s
WHERE points = 0;
DELETE FROM input_u
WHERE points = 0;

# Ratio filtering: of the riders left, keep the top scoring few.
INSERT INTO output_ar
SELECT *
FROM input_ar
WHERE points >= 800 AND points/cost >= 70.0
ORDER BY cost DESC, points DESC;
INSERT INTO output_c
SELECT *
FROM input_c
WHERE points >= 700 AND points/cost >= 50.0
ORDER BY cost DESC, points DESC;
INSERT INTO output_s
SELECT *
FROM input_s
WHERE points/cost >= 70.0
ORDER BY cost DESC, points DESC;
INSERT INTO output_inter
SELECT *
FROM input_u
ORDER BY points DESC
LIMIT 32;
INSERT INTO output_u
SELECT *
FROM output_inter
ORDER BY cost DESC, points DESC;

 # Make up the table which will be used to output the wildcard file. 
INSERT INTO output_w
SELECT * FROM output_ar;
INSERT INTO output_w
SELECT * FROM output_c;
INSERT INTO output_w
SELECT * FROM output_s;
INSERT INTO output_w
SELECT * FROM output_u;

# Output the results into the output files. 
SELECT 'Names', 'Cost', 'Points'
UNION ALL
	SELECT * FROM output_ar
    INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/France_AllRounder_Top.txt'
	FIELDS TERMINATED BY ',' ENCLOSED BY ''
	LINES STARTING BY '' TERMINATED BY '\n';
SELECT 'Names', 'Cost', 'Points'
UNION ALL
	SELECT * FROM output_c
    INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/France_Climber_Top.txt'
	FIELDS TERMINATED BY ',' ENCLOSED BY ''
	LINES STARTING BY '' TERMINATED BY '\n';
SELECT 'Names', 'Cost', 'Points'
UNION ALL
	SELECT * FROM output_s
    INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/France_Sprinter_Top.txt'
	FIELDS TERMINATED BY ',' ENCLOSED BY ''
	LINES STARTING BY '' TERMINATED BY '\n';
SELECT 'Names', 'Cost', 'Points'
UNION ALL
	SELECT * FROM output_u
    INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/France_Unclassified_Top.txt'
	FIELDS TERMINATED BY ',' ENCLOSED BY ''
	LINES STARTING BY '' TERMINATED BY '\n';
SELECT 'Names', 'Cost', 'Points'
UNION ALL
	SELECT * FROM output_w
    INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/France_Wildcard_Top.txt'
	FIELDS TERMINATED BY ',' ENCLOSED BY ''
	LINES STARTING BY '' TERMINATED BY '\n';