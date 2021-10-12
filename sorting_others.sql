# This code is used to select the best-scoring riders for the Classics Squad contests.

# Clear the tables of the old data.
DELETE FROM input;
DELETE FROM output_inter;
DELETE FROM output;

# Load the data.
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Liege_Bastogne_Liege.csv'
INTO TABLE input
FIELDS TERMINATED BY ',' ENCLOSED BY ''
LINES STARTING BY '' TERMINATED BY '\n'
IGNORE 1 ROWS;

# Keep the highest scoring riders.
INSERT INTO output_inter
SELECT * FROM input
ORDER BY points DESC
LIMIT 25;

# Format the outputs.
INSERT INTO output
SELECT * FROM output_inter
ORDER BY cost DESC, points DESC;

# Output the results into the output file.
SELECT 'Names', 'Cost', 'Points'
UNION ALL
	SELECT * FROM output
    INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Liege_Bastogne_Liege.txt'
	FIELDS TERMINATED BY ',' ENCLOSED BY ''
	LINES STARTING BY '' TERMINATED BY '\n';