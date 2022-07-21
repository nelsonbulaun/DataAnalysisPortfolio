import requests
from settings import Settings
from models import PlayerGeneralTraditionalPerGamePositions

settings = Settings()
settings.db.create_tables([PlayerGeneralTraditionalPerGamePositions], safe=True)
headers  = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}
position_list = [
    'G',
    'F',
    'C'
]   
season_list = [
    '1996-97',
    '1997-98',
    '1998-99',
    '1999-00',
    '2000-01',
    '2001-02',
    '2002-03',
    '2003-04',
    '2004-05',
    '2005-06',
    '2006-07',
    '2007-08',
    '2008-09',
    '2009-10',
    '2010-11',
    '2011-12',
    '2012-13',
    '2013-14',
    '2014-15',
    '2015-16',
    '2016-17',
    '2017-18',
    '2018-19',
    '2019-20',
    '2020-21',
    '2021-22'
]

#Select statistics duration type to be taken from the table:
#per_mode = 'Per100Possessions'
#per_mode = 'Totals'
#per_mode = 'Per36'
per_mode = 'PerGame'

# Module used to scrape data from the website
# for loop to scrape data of each season on the list
for season_id in season_list:
    # We find that player's position within the table returns a null value, thus making us unable to take copy it from the table. To get around this we alter the url to filter through each position and produce the stats of each player who plays that position. We use a for loop to change the filter settings to specify each position, scrape data on every character that can be seen at that position, and append the found position to the player's statistics.
    for player_position in position_list:
        print("Now working on "+season_id+ " season position:"+player_position)
        # going to the nba stats page and inspecting elements, we find this nba stats url to scrape the data from
        player_info_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=' + per_mode +'&Period=0&PlayerExperience=&PlayerPosition=' + player_position + '&PlusMinus=N&Rank=N&Season=' + season_id + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='
        # json response
        response = requests.get(url=player_info_url, headers=headers).json()
        # we pull the data for the statistics for each player
        player_info = response['resultSets'][0]['rowSet']
        # loops over data to insert into table
        for row in player_info:
            player = PlayerGeneralTraditionalPerGamePositions(
                season_id=season_id,
                player_position=player_position, 
                PLAYER_ID=row[0],
                PLAYER_NAME=row[1],
                NICKNAME=row[2], 
                TEAM_ID=row[3],
                TEAM_ABBREVIATION=row[4],
                AGE=row[5],
                GP=row[6],
                W=row[7],
                L=row[8],
                W_PCT=row[9],
                MIN=row[10],
                FGM=row[11],
                FGA=row[12],
                FG_PCT=row[13],
                FG3M=row[14],
                FG3A=row[15],
                FG3_PCT=row[16],
                FTM=row[17],
                FTA=row[18],
                FT_PCT=row[19],
                OREB=row[20],
                DREB=row[21],
                REB=row[22],
                AST=row[23],
                TOV=row[24], 
                STL=row[25],
                BLK=row[26],
                BLKA=row[27],
                PF=row[28],
                PFD=row[29],
                PTS=row[30],
                PLUS_MINUS=row[31],
                NBA_FANTASY_PTS=row[32],
                DD2=row[33],
                TD3=row[34],
                WNBA_FANTASY_PTS=row[35],
                GP_RANK=row[36],
                W_RANK=row[37],
                L_RANK=row[38],
                W_PCT_RANK=row[39],
                MIN_RANK=row[40],
                FGM_RANK=row[41],
                FGA_RANK=row[42],
                FG_PCT_RANK=row[43],
                FG3M_RANK=row[44],
                FG3A_RANK=row[45],
                FG3_PCT_RANK=row[46],
                FTM_RANK=row[47],
                FTA_RANK=row[48],
                FT_PCT_RANK=row[49],
                OREB_RANK=row[50],
                DREB_RANK=row[51],
                REB_RANK=row[52],
                AST_RANK=row[53],
                TOV_RANK=row[54],
                STL_RANK=row[55],
                BLK_RANK=row[56],
                BLKA_RANK=row[57],
                PF_RANK=row[58],
                PFD_RANK=row[59],
                PTS_RANK=row[60],
                PLUS_MINUS_RANK=row[61],
                NBA_FANTASY_PTS_RANK=row[62],
                DD2_RANK=row[63],
                TD3_RANK=row[64],
                WNBA_FANTASY_PTS_RANK=row[65],
                CFID=row[66],
                CFPARAMS=row[67])
            
            player.save()
        
print ("Done inserting player general traditional positions season per game data to the database!")


