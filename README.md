# velogames-ultimate-team

Introduction on Velogames:

Velogames is a fantasy cycling platform, where users pick riders to make a team, while staying within a credit limit.
These riders then earn points depending on their performances in races.
There are lots of different events and event types:

- Superclasico: a season-long event, covering the biggest men's one-day races (usually 30+ races) of the calendar. Each team of 6 can be completely changed between each race.
- Women's Classics: the women's Superclasico, also with 6 rider teams. This didn't happen in 2020.
- Classics Squad: similar to Superclasico, but with notable differences. This also covers a series of one-day races (12 ish), but only the spring ones, usually starting with Milano-Sanremo and finishing with Liège-Bastogne-Liège. Users create a squad of 12 riders, which is to be kept for the entire campaign. However, there is a substitution allowance, which can be used between races however we deem fit, as long as we don't exceed our total for the entire event. This event is usually only for men's races, though there was a women's edition in 2020.
- Stage Races: there is a separate event for each major week-long stage race, where 9 riders fill your team.
- Grand Tours: the biggest stage races of the year. There are three of them, and each lasts three weeks. There are 9 riders in each team, but riders are now given a class: All Rounder, Climber, Sprinter or Unclassified. Teams must comprise 2 All Rounders, 2 Climbers, 1 Sprinter, 3 Unclassified riders and 1 'Wildcard' who can be any other rider from any class.


Finding the best team:

Once the final results for the latest event are uploaded, a database is written up containing the names, credit cost and points scored for either all scoring riders (for one day races) or for all riders who took part (for longer races).
These databases are saved in .csv format in the folder corresponding to the event type and year.
Determining the best team for most Velogames events is now done using two Jupyter notebook scripts: VUTfiltering and VUTfinder.

The first step is to filter the database and keep only the best-scoring riders.
This hugely reduces the number of possible combinations that the finder program will run, which speeds up the run time.
The filtering is done in two ways, which I call logical filtering and ratio filtering:

- Logical filtering: this limits the number of saved riders for each cost value. In a 6 rider team, there can never be more than 6 equal-costing riders, so keeping the 7th best-scoring rider would be useless. This is especially effective for the Grand Tour events.
- Ratio filtering: this only keeps the riders that have reached a set points/cost ratio. This kind of filtering removes high-costing but low-scoring riders, that logical filtering couldn't remove. Work is still ongoing to find the ratios that lead to the best balance of filtering.

Once the filtering is complete, the kept riders are outputted into a 'race_name_filtered.txt' file, which is to be read into the finder program.
The finder code runs through all the possible combinations, checking if they stay within the credit limit, and saves the best scoring combination.
This combination is then outputted into another text file, called 'race_name_UT.txt'.
The best team is also recorded in an Excel file 'VUT_year.xlsx', which holds all the best teams for all the Velogames events of the year, and also contains some extra data.
The functions used in these two algorithms are saved in the Python 'VUTfunctions.py' file.

This method works for almost all 2022 Velogames events, with the exception of the Grand Tours and the Ultimate Squad:

- Grand Tours: because of the introduction of riders classes, this slightly changes the filtering process and how the combinations are worked out, so seperate algorithms are used: GTfiltering and GTfinder. A few functions from the VUTfunctions file are still used.
- Ultimate Squad: this is the best possible squad for the Classics Squad event as a whole, including substitutions. The best team for each individual Classics Squad race is found using the VUT files, but finding the best squad requires a much more intricate process, meaning different files: USfunctions, USfiltering and USfinder. However, because of the sheer size of the task, I have never tried to find the ultimate squad for any entire event yet, it would just take too long. I know the process works, having successfully tested it on a much smaller handmade sample. I am hopeful of still being able to use these codes on the actual datasets.


In 2020 and 2021, individual codes were used for each event type, and filtering was done using SQL files.
These files are present in the Archive_Files folder.

The Test_Files folder holds files I used to test processes during the writing of codes, including the test sample used to check the working of the Ultimate Squad finder code.
