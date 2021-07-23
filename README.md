# velogames-ultimate-team

Velogames is a fantasy cycling competition, where users create their team for a race and pick their riders, while staying within a credit limit. At the end of the race, scores are given to each rider depending on race results.
I started using Velogames in 2020, and I wanted to see if I could write code to determine what the best possible team for a race was, using the scores given at the end of the event.

I got the idea during the Giro d'Italia (Italy event on Velogames), and so I first started working on code to work on results from the Grand Tours.
The Grand Tours are the Giro d'Italia, the Tour de France and the Vuelta a Espana, and their respective events on Velogames are Italy, France and Spain.
Once I had working Python code, I moved on to find the best teams for the other Velogames events.
The teams' composition changes for different events, so I decided to write new programs for each event type, for the sake of clarity.
The different event types are:

- Grand Tours: each team comprises 9 riders, but riders are split into classes. Players must pick 2 All Rounders, 2 Climbers, 1 Sprinter and 3 Unclassified riders, as well as 1 Wildcard, who can be any rider from any class.
- Stage Races: each team is made up of 9 riders. These races are week-long World Tour level stage races, such as Paris-Nice or the Tour de Romandie
- Superclasico: each team is made up of 6 riders. These are one day races, including Monuments, World Tour level and smaller races.
- Women's Classics: each team is made up of 6 riders. This is essentially the Women's equivalent of the Superclasico. This event type did not happen in 2020, but was instead a short Classics Squad event.
- Classics Squad: this is a series of the major one day races held in the Spring, where players create a squad of 12 riders, which they keep throughout the whole event, though a limited number of substitutions are available. 


Note on the Classics Squad:

I have written code to determine the best squad for the Classics Squad events, including substitutions, but I do not have the processing power to run it without it taking weeks. I know the code works, because I have used a small handmade sample to test my program.
For this event, I determine the best 12 man team for each individual race.


How the code works:


I write the results of each race as databases saved in CSV files.
These files are read into a Python code, and each combination is tested to see if it is within the credit limit and its points total calculated.
If the combination's points total surpasses the current best, its composition, cost total and points total are saved in variables.
Once all the combinations have been evaluated, the best team's rider composition is outputted into a text file, along with how much it cost and scored.

For most of the races, the number of combinations to evaluate (especially if the teams have 9 riders) is high, leading to long (several hours) run times.
To speed this up, I wrote some SQL files, which would sort through the results and remove the lower-scoring riders, who would not be in the best team.
I used two types of filtering, depending on the event type.

- Ratio filtering: only keep riders who have a points to cost ratio above a threshhold.
- Logical filtering: used for the Grand Tour races. Because you are limited in the number of riders to pick from each class, for each cost only keep the best scoring (2 All Rounders, 2 Climbers, 1 Sprinter, 3 Unclassified + 1 each for the Wildcard) of riders.


Extra files and folders:
- The Test Files folder contains files I used to test different processes and figure issues out.
- The Points Ratio Excel files were used for some data analysis to determine the best threshhold values for the ratio filtering in the SQL files.
- The VUT_2020 and VUT_2021 Excel files are my results files, holding details for each race, including the number of riders in the databases, before and after filtering, and the result outputs.


Note:
I worked on the Ultimate Squad file after the others, and it took a lot of effort to get working properly.
I could use some of the more optimised processes from it and apply them to the others to update them.
I might do this in the future, but for now I do not see the need
