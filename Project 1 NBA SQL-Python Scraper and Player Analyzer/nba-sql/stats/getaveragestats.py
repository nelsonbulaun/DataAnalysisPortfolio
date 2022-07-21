#!/usr/bin/python
#!/usr/bin/env python
from __future__ import print_function
from audioop import avg
import pymysql
import pandas

hostname = 'localhost'
username = 'root'
password = 'password123!'
database = 'nba_stats'

playerpos_list = [
  ' IS NOT NULL ',
  "='G' ",
  "='F' ",
  "='C' "
]

catagory_list = [
  'fg3m',
  'fg_pct',
  'ft_pct', 
  'reb/gp',
  'ast/gp',
  'tov/gp',
  'stl/gp',
  'blk/gp',
  'pts/gp'
]
con = pymysql.connect(
  host=hostname,
  user=username,
  password=password,
  database=database
)

class PlPosition:
    __slots__ = ['name','position', 'fg3m', 'fg_pct' ,'ft_pct' , 'reb', 'ast', 'tov', 'stl', 'blk', 'pts']
    def __init__(self, name, position ,fg3m, fg_pct ,ft_pct , reb, ast, tov, stl, blk, pts):
        self.name=name
        self.position=position
        self.fg3m=fg3m
        self.fg_pct=fg_pct
        self.ft_pct=ft_pct
        self.reb = reb
        self.ast = ast
        self.tov = tov
        self.stl = stl
        self.blk = blk
        self.pts = pts

    def as_dict(self):
        return {
          'name': self.name, 
          'position': self.position,
          'Three Pointers Made': self.fg3m, 
          'Fieldgoal Percentage': self.fg_pct, 
          'freethrow percentage':self.ft_pct, 
          'Rebounds':self.reb, 
          'Assists':self.ast, 
          'Turonovers':self.tov, 
          'Steals':self.stl , 
          'Blocks':self.blk, 
          'Points':self.pts,
          }


def nameplayerposition(pos):
  if pos==' IS NOT NULL ':
    return ("All",)
  elif pos=="='G' ":
    return ("Guard",)
  elif pos=="='F' ":
    return ("Forward",)
  elif pos=="='C' ":
    return ("Center",)

def playerposition(pos):
  if pos==' IS NOT NULL ':
    return ("All",)
  elif pos=="='G' ":
    return ("G",)
  elif pos=="='F' ":
    return ("F",)
  elif pos=="='C' ":
    return ("C",)


#Builds average for each catagory for everyone in the league, as well as at each position (guard, forward and center)
testb = []
try:
    with con.cursor() as cur:
        for playerpos in playerpos_list:
          testa=[]
          for catagory in catagory_list:
            test1 = ("SELECT avg("+catagory+") FROM nba_stats.player_general_traditional_totals_positions WHERE player_position"+playerpos+"AND season_id='2021-22' AND min/gp>'20'") 
            cur.execute(test1)
            rows = cur.fetchall()
            if catagory=='fg3m' :
              testa.extend([nameplayerposition(playerpos), playerposition(playerpos),rows[0]])
            else:
              testa.append(rows[0])
              y = [i[0] for i in testa]
          testb.append(y)

finally:

  con.close()

ListOfStatPositions = [PlPosition(*z) for z in testb]
# print(ListOfStatPositions[0])

# AvgPlayer = ListOfStatPositions[0]
# AvgGuard = ListOfStatPositions[1]
# AvgForward = ListOfStatPositions[2]
# AvgCenter = ListOfStatPositions[3]
# print(AvgPlayer.blk)
# print(AvgGuard.blk)
# print(AvgForward.blk)
# print(AvgCenter.blk)


