#!/usr/bin/python
#!/usr/bin/env python
from __future__ import print_function
from audioop import avg
import pymysql
import pandas

from getaveragestats import PlPosition, catagory_list

hostname = 'localhost'
username = 'root'
password = 'password123!'
database = 'nba_stats'


playerdata = []
namedata = []

testlist = ["Joel Embiid" , "Stephen Curry", "Seth Curry"]



def makeplayers(listofplayers):
  playerssearched = []
  for pdata in listofplayers:
    playerselected = PlPosition(pdata[0], pdata[1], pdata[2], pdata[3], pdata[4], pdata[5], pdata[6], pdata[7], pdata[8], pdata[9], pdata[10])
    playerssearched.append(playerselected)
  return(playerssearched)

def getplayersstats(listofnames):
  con = pymysql.connect(
  host=hostname,
  user=username,
  password=password,
  database=database)
  try:
    with con.cursor() as cur:
      for fname in listofnames:
          testa=[]
          for catagory in catagory_list:
            test1 = ("SELECT avg("+catagory+") FROM nba_stats.player_general_traditional_totals_positions WHERE player_name= '"+fname+"' AND season_id='2021-22'")
            test2 = ("SELECT player_name FROM nba_stats.player_general_traditional_totals_positions WHERE player_name= '"+fname+"' AND season_id='2021-22'")
            test3 = ("SELECT player_position FROM nba_stats.player_general_traditional_totals_positions WHERE player_name= '"+fname+"' AND season_id='2021-22'")
            if catagory == 'fg3m':
              cur.execute(test2)
              rowa = cur.fetchall()
              cur.execute(test3)
              rowb = cur.fetchall()            
              cur.execute(test1)
              rowc = cur.fetchall()
              testa.extend([rowa[0], rowb[0], rowc[0]])
            else:
              cur.execute(test1)
              rows = cur.fetchall()
              testa.append(rows[0])
              # print(testa)
          y = [i[0] for i in testa]
          playerdata.append(y)
          print(playerdata)
    return makeplayers(playerdata)
                    
  finally:
    con.close()
  



#a = getplayersstats(testlist)
#print(a)

#a=(getplayerstats('Joel Embiid'))
#print(a)
#print(a.position)

