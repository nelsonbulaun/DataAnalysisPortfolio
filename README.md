<div id="top"></div>

[![LinkedIn][linkedin-shield]][linkedin-url]
[![Google Analytics][Google-analytics.js]][Google-analytics-Certification-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<!--  <a href="https://github.com/nelsonbulaun/DataAnalysisPortfolio">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
 -->
<h3 align="center">Data Analysis Portfolio</h3>

  <p align="center">
    A repository to display my previous data analysis projects and experiences.
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  <!--  <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p> 
  -->
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#project-1">Project 1</a>
      <ul>
        <li><a href="#programs-used1">Programs Used</a></li>
        <li><a href="#required-files1">Required Files</a></li>
        <li><a href="#description1">Description</a></li>
      </ul>
    </li>
    <li>
      <a href="#project-2">Project 2: </a>
      <ul>
        <li><a href="#programs-used1">Programs Used</a></li>
        <li><a href="#required-files1">Required Files</a></li>
        <li><a href="#description1">Description</a></li>
      </ul>
    </li>
    <li>
      <a href="#project-3">Project 3: </a>
      <ul>
        <li><a href="#programs-used1">Programs Used</a></li>
        <li><a href="#required-files1">Required Files</a></li>
        <li><a href="#description1">Description</a></li>
      </ul>
    </li>
    <li><a href="#school">Resume And Certifications</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->

## **Project 1: [NBA Stat Scraper/Compare Tool](/Project%202%20Divvy%20Trip%20Analysis)** <a name="project-1"></a>
### Programs Used/Needed:
[![Python.js][Python.js]][Python-url] [![MySQL.js][MySQL.js]][MySQL-url] [![Tableau.js][Tableau.js]][Tableau-url]

### Required Files
* [NBA Stat Scraper/Compare Tool](/Project%202%20Divvy%20Trip%20Analysis) _(File section/breakdown can be found in later section)_ 

### Description: 
A project consisting of three parts, a script that scrapes data from the official nba statistics website storing it into an SQL database, a script using multiple user-made functions to access the database and compare player statistics with posiotional averages, and a tableau dashboard (which is currently being expanded) that provides useful statistics and information to aid in fantasy basketball.  <br>

### Introduction:
Fantasy basketball is a game in which the each participant drafts and serves as owners of a their own virtual NBA team . There are two types of fantasy basketball leagues that are run, fantasy points leagues, which are significantly more simple, and category leagues (AKA. "Cat Leagues") In simple terms, categorical fantasy leagues work as follows. Each week a player faces a new team, where the winner is decided by whoever's team has a higher total in more categories than their opponent. These categories are points, rebounds, assists, steals, blocks, threes, Field Goal% Free throw%, and turnovers. When the week begins owners set up their active roster, usually around 10 players that the owners want to play, with restrictions limiting player selection based on their position. Usually an active roster is allowed to play 1 Point Guard, 1 Shooting Guard, 1 Small Forward, 1 Power Forward, 1 Center, and around 5 "bench" slots that allow for any position to be played. Towards the beginning of the official NBA season, fantasy basketball drafts occur, where each individual selects the members of their team, most leagues will have a limit to the number of players per position. The fantasy basketball draft is THE PIVOTAL MOMENT of every fantasy league, as the players you select will typically be on your team for the entirety of the season, thereby dictating whether a person will win the season. That’s where this project comes in. Historically, I am inconsistent in this situation, and find myself either doing well or absolutely horrid, so I decided to make a script that'll help me pick players for my team and demolish every league I enter.

### Breakdown:
The project consists of three parts:
1. creating/modifying a python script that scrapes player statistic data from the nba website then stores it into an SQL Database, 
2. a script that accesses the aforementioned database to compare their stats with the league average for players who share the same position, and 
3. the third which does something similar to the second, but uses tableau instead of pandas to take data and create graphics for each of the stats <br>

### Part 1: SQL Webscraper <br>
This script is a modified/updated variation of https://jman4190.medium.com/building-an-nba-mysql-database-with-python-c653fa15333c changing the function that takes the headers, that sort out the order of the column and what data they represent, to be inclusive of stats that were previously not apart of the tables as well as storing an additional column that gives each players position. _A short description of each script used within this part of the project can be found below, with commented notes within telling the purpose of each line._ <br>


**Associated Files** <br>
[stats](/Project%201%20NBA%20SQL-Python%20Scraper20and%20Player%20Analyzer/stats/) - the containing folder
* [settings.py](/Project%201%20NBA%20SQL-Python%20Scraper20and%20Player%20Analyzer/stats/settings.py) - is used as a reference in other scripts to initiate the SQL database to connect and create tables 
* [player_general_traditional_totals_position.py](/Project%201%20NBA%20SQL-Python%20Scraper20and%20Player%20Analyzer/stats/player_general_traditional_totals_positions.py) - The script that is used in scraping data, this takes the nba statistics data table via. url, and creates an object with model class "PlayerGeneralTraditionalTotalPositions". It then assigns each row to fit the appropriate statistic of each player and stores it in the data table. 
* [Models](/Project%201%20NBA%20SQL-Python%20Scraper20and%20Player%20Analyzer/stats/Models/)- acts as a dict containing 
    * [\_\_init\_\_](/Project%201%20NBA%20SQL-Python%20Scraper20and%20Player%20Analyzer/stats/Models/__init__.py) - tells where each module within a folder is located
    * [BaseModel](/Project%201%20NBA%20SQL-Python%20Scraper20and%20Player%20Analyzer/stats/Models/BaseModel.py) - used in the creation of new classes, with the the purpose of passing the database to each class that is generated
    * [PlayerGeneralTraditionalTotalPositions](/Project%201%20NBA%20SQL-Python%20Scraper20and%20Player%20Analyzer/stats/Models/PlayerGeneralTraditionalTotalPositions.py) - A created class that defines each different statistic of a player as an element, specifying their field types and assigning the class to each player in the final webscraping script. 

### Part 2: Player/Position Average Stat graber <br>
Upon downloading the NBA SQL webscraper, attached are 3 scripts, that work together to run the player compare table script. This is a quick way to access the data that was stored in the previous section with the purpose of grabbing a specific player's stats, as well as the average stats at each position, and creating a table to compare the two sets.

**Associated Files:**<br>
[stats](/Project%201%20NBA%20SQL-Python%20Scraper20and%20Player%20Analyzer/stats/) - the containing folder
* [getaveragestats.py](/Project%201%20NBA%20SQL-Python%20Scraper20and%20Player%20Analyzer/stats/getaveragestats.py) - Initiates the database, creating a list of four objects, all, guard, forward, and Center, consisting of each position's average statistics for each of the fantasy basketball catagories.
taking all data where the based on player 
* [getplayerstats.py](/Project%201%20NBA%20SQL-Python%20Scraper20and%20Player%20Analyzer/stats/getplayerstats.py) - Script that takes in a player's name and initiates the database, creating an object with the player's stats at each catagory. 
* [playercomparetable.py](/Project%201%20NBA%20SQL-Python%20Scraper20and%20Player%20Analyzer/stats/playercomparetable.py) - Input a player's name and uses the two functions:  [getaveragestats.py](/Project%201%20NBA%20SQL-Python%20Scraper20and%20Player%20Analyzer/stats/getaveragestats.py), and [getplayerstats.py](/Project%201%20NBA%20SQL-Python%20Scraper20and%20Player%20Analyzer/stats/getplayerstats.py), to create a list consisting of a player and the average statistics at each position. The script then uses the pandas module to make a table consisting of each object in the list. 

### Part 3: Tableau <br> 
Initially I had wanted to access the database through Tableau but I without a premium membership I was unable to do such so I exported the the data from the SQL database into a .csv file. After doing this I created a few simple visualizations/tables that showed a variety of information that would be useful in deciding if a player would be useful or not.

**Associated Files** <br>

* https://public.tableau.com/app/profile/nelson.bulaun/viz/NBAPlayerStatistics_16585735629620/PlayerAveragesvsPositionalAverages#1
* https://public.tableau.com/app/profile/nelson.bulaun/viz/NBAPlayerStatistics2/PlayerStatistics
* https://public.tableau.com/app/profile/nelson.bulaun/viz/NBAPlayerStatistics_16585735629620/PlayerAveragesvsPositionalAverages

_Relevent Skills Used: web scraping, creating databases, importing data into Databases (SQL), Making Query's_
<p align="right">(<a href="#top">back to top</a>)</p>

## Project 2: [RCP Research Analysis](/Project%201%20RCP%20Research%20Analysis) <a name="project-2"></a>
### Programs Used/Needed:
[![MATLAB.js][MATLAB.js]][MATLAB-url]

### Required Files
* [RCP Data Analysis.mlx](/Project%201%20RCP%20Research%20Analysis/RCP%20Data%20Analysis.mlx)
* [climateStationData.csv](/Project%201%20RCP%20Research%20Analysis/climateStationData.csv)
* [ClimateModelDataAnnual.csv](/Project%201%20RCP%20Research%20Analysis/ClimateModelDataAnnual.csv)

### Description
A University research project with the goal of finding the correlation between a climate model's estimated green house gass effect and real world data. This is completed through regression analysis between the yearly precipitation levels on data measured at the Vancouver Harbour Weather Station and Vancouver's predicted precipitation by the CMIP5 climate model. Through this research we found that we are unable to confidently state that there is a strong correlation between each of the models and the actual data taken.  <br>

### Background Information: 
Looking into models, we chose the CMIP5 climate mode which is a coordinated climate modeling exercise involving 20 climate-modeling groups from around the world and has provided a standard experimental protocol for producing and studying the output of many different global climate models.  From the CMIP5 climate models, we chose datasets relating to different Representative Concentration Pathways (RCP), which represents scenarios with different concentrations of greenhouse gas (GHG) emissions, which allows scientists to model climate change to build scenarios about the impacts of climate change and to help plan for the future. 

### Sample Figures: 
Shown below are some of the figures that were produced within the script as a visualization for the comparissons in values between various datasets.

<div align="center">
    
![image](https://user-images.githubusercontent.com/108250880/180628108-a7080bc8-e62e-4cec-a4be-d6af478f7986.png)
![image](https://user-images.githubusercontent.com/108250880/180628084-1e64a99c-d474-449a-9e14-c9809e8ad903.png)
![image](https://user-images.githubusercontent.com/108250880/180628095-f01dc817-3062-4d3f-a6f4-acf481bfe2ea.png)
    
 </div>
 
Relevent Skills Used: web scraping, creating databases, importing data into Databases (SQL), Making Query's
<p align="right">(<a href="#top">back to top</a>)</p>

  

## **Project 3: [Divvy Trips Analysis](/Project%202%20Divvy%20Trip%20Analysis)** <a name="project-3"></a>
### Programs Used/Needed:
[![R.js][r.js]][r-url] [![Tableau.js][Tableau.js]][Tableau-url]
### Required Files
* [DivvyTripsCaseStudy.R](/Project%202%20Divvy%20Trip%20Analysis/DivvyTripsCaseStudy.R) [202XXX-divvy-tripdata.rar](/Project%202%20Divvy%20Trip%20Analysis)  (from 2021-06 to 2022-05) (Included in project folder)
### Description: 
Google Analytics Case Study Project that analyzes data for a fictional bike-share company with the purpose of attracting more riders. The case study files are split into two sections R and Tableau. Initially, the R file, provided by google and set up by Kevin Hartman, was filled with outdated data which acts as skeleton for the user to follow with the purpose developing and displaying a basic understanding of data analysis tasks. The file attached is the updated variation, substituting datasets and cleaning them based upon the differences between the two. This demonstrates the ability to import and combine data sets, clean them to be ready for analysis, then lastly compare the variables from each of the datasets and plot them out. 
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Schooling, Resume, and Certifications <a name="school"></a>
[![LinkedIn][linkedin-shield]][linkedin-url] [![Google Analytics][Google-analytics.js]][Google-analytics-Certification-url] \
University Of British Columbia, B.Sc in Combined Major in Science (Physics, Chemistry, and Mathematics) \
Google Data Analytics Certification: https://coursera.org/share/930192e89d10a668ebb6a215953d00e8 \
Resume:[NelsonBulaunResume.pdf](/NelsonBulaunResume.pdf) 


<p align="right">(<a href="#top">back to top</a>)</p>





<!-- [<BRAND>.js]: https://img.shields.io/badge/<TEXT>-000000?style=for-the-badge&logo=<LOGO>&logoColor=blue -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://linkedin.com/in/linkedin_username
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[R.js]: https://img.shields.io/badge/R-000000?style=for-the-badge&logo=r&logoColor=blue
[R-url]: https://www.r-project.org/
[Python.js]: https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=green
[Python-url]:https://www.python.org/
[Tableau.js]: https://img.shields.io/badge/Tableau-5F889C?style=for-the-badge&logo=tableau&logoColor=white
[Tableau-url]: https://www.tableau.com/
[MySQL.js]: https://img.shields.io/badge/MySQL-000000?style=for-the-badge&logo=MySql&logoColor=white
[MySQL-url]: https://www.mysql.com/
[MATLAB.js]: https://tinyurl.com/matlablogo
[MATLAB-url]: https://www.mathworks.com/
[Google-Analytics.js]: https://img.shields.io/badge/Google%20Analytics-E37400?style=for-the-badge&logo=google%20analytics&logoColor=white
[Google-Analytics-Certification-url]: https://coursera.org/share/930192e89d10a668ebb6a215953d00e8 

[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors

[product-screenshot]: images/screenshot.png
