# This code is used to select the best-scoring riders for the Stage Race contests.

# Clear the tables of the old data.
DELETE FROM input;
DELETE FROM output;

# Load the data.
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Giro_Donne.csv'
INTO TABLE input
FIELDS TERMINATED BY ',' ENCLOSED BY ''
LINES STARTING BY '' TERMINATED BY '\n'
IGNORE 1 ROWS;

# Remove any rider who didn't score. 
DELETE FROM input
WHERE points = 0;

# Ratio filtering: of the riders left, keep the top scoring few.
# Set ratio to 10 for Madrid Challenge as it is a much shorter race, otherwise 20.
DELETE FROM input
WHERE points/cost < 20.0;

# Logical filtering: keep a top-scoring number of riders for each cost. 
CALL filtering(32, 9);

# Output the results into the output file.
SELECT 'Name', 'Cost', 'Points'
UNION ALL
	SELECT * FROM output
    INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Giro_Donne.txt'
	FIELDS TERMINATED BY ',' ENCLOSED BY ''
	LINES STARTING BY '' TERMINATED BY '\n';