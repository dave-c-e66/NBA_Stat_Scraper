# NBA_Stat_Scraper

# Request Data
To request data you put the name of the NBA player who's salary you want in a text file called player_name.txt.
The name should match how the name is formatted on https://www.basketball-reference.com/contracts/players.html

For example you would write "LeBron James" to player_name.txt if you wanted his salary.

Only 1 players name should be written to the file.

# Receive Data
The salary for the player who's name was in the player_name.txt file will be written into the player_salary.txt file.
The salary returned is for the most recent year, currently 2022/2023 season.
The salary will have dollar signs and comma's.

For example if "LeBron James" was written in the player_name.txt file the following would be in the player_salary.txt file:
$44,474,988

# UML Sequence Diagram

![Untitled Diagram drawio](https://user-images.githubusercontent.com/55772436/180630063-f67bb5e6-c20e-4890-a873-2861c640c50d.png)
