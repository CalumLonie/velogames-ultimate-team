# This code is used to select the best scoring riders to determine the ultimate team in the
# Grand Tour contests.

# Clear the tables of old data. 
DELETE FROM input_ar;
DELETE FROM input_c;
DELETE FROM input_s;
DELETE FROM input_u;
DELETE FROM output_ar;
DELETE FROM output_c;
DELETE FROM output_s;
DELETE FROM output_u;
DELETE FROM output_w;

# Load the data. 
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Spain_AllRounder.csv'
INTO TABLE input_ar
FIELDS TERMINATED BY ',' ENCLOSED BY ''
LINES STARTING BY '' TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Spain_Climber.csv'
INTO TABLE input_c
FIELDS TERMINATED BY ',' ENCLOSED BY ''
LINES STARTING BY '' TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Spain_Sprinter.csv'
INTO TABLE input_s
FIELDS TERMINATED BY ',' ENCLOSED BY ''
LINES STARTING BY '' TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Spain_Unclassified.csv'
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

# Logical filtering: keep a top-scoring number of riders for each cost. 
CALL filtering_ar (26);
CALL filtering_c (26);
CALL filtering_s (26);
CALL filtering_u (26);

# Ratio filtering: of the riders left, keep the top scoring few.
DELETE FROM output_ar
WHERE points/cost < 80.0;
DELETE FROM output_c
WHERE points/cost < 80.0;
DELETE FROM output_s
WHERE points/cost < 80.0;
DELETE FROM output_u
WHERE points/cost < 80.0;

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
    INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Spain_AllRounder_Ultimate.txt'
	FIELDS TERMINATED BY ',' ENCLOSED BY ''
	LINES STARTING BY '' TERMINATED BY '\n';
SELECT 'Names', 'Cost', 'Points'
UNION ALL
	SELECT * FROM output_c
    INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Spain_Climber_Ultimate.txt'
	FIELDS TERMINATED BY ',' ENCLOSED BY ''
	LINES STARTING BY '' TERMINATED BY '\n';
SELECT 'Names', 'Cost', 'Points'
UNION ALL
	SELECT * FROM output_s
    INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Spain_Sprinter_Ultimate.txt'
	FIELDS TERMINATED BY ',' ENCLOSED BY ''
	LINES STARTING BY '' TERMINATED BY '\n';
SELECT 'Names', 'Cost', 'Points'
UNION ALL
	SELECT * FROM output_u
    INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Spain_Unclassified_Ultimate.txt'
	FIELDS TERMINATED BY ',' ENCLOSED BY ''
	LINES STARTING BY '' TERMINATED BY '\n';
SELECT 'Names', 'Cost', 'Points'
UNION ALL
	SELECT * FROM output_w
    INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Spain_Wildcard_Ultimate.txt'
	FIELDS TERMINATED BY ',' ENCLOSED BY ''
	LINES STARTING BY '' TERMINATED BY '\n';