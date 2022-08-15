from __future__ import print_function
from audioop import avg
import pymysql
import pandas as pd
import jinja2
import matplotlib
import matplotlib.cm

from getaveragestats import PlPosition
from getaveragestats import ListOfStatPositions
from getplayerstats import getplayersstats

CatList = ["Three Pointers Made",  
    "Fieldgoal Percentage", 
    "Freethrow Percentage", 
    "Rebounds",
    "Assists",
    "Turnovers",
    "Steals", 
    "Blocks",
    "Points"
]


def background_with_norm(s):
    cmap = matplotlib.cm.get_cmap('RdYlGn')
    norm = matplotlib.colors.TwoSlopeNorm(vmin=s[0]*0.75, vcenter=s[0], vmax=s[0]*1.25)
    #norm = matplotlib.colors.TwoSlopeNorm(vmin=s[1]*0.75, vcenter=s[1], vmax=s.values.max())
    return ['background-color: {:s}'.format(matplotlib.colors.to_hex(c.flatten())) for c in cmap(norm(s.values))]

def background_with_normto(s):
    cmap = matplotlib.cm.get_cmap('RdYlGn_r')
    norm = matplotlib.colors.TwoSlopeNorm(vmin=s[0]*0.75, vcenter=s[0], vmax=s[0]*1.25)
    #norm = matplotlib.colors.TwoSlopeNorm(vmin=s[1]*0.75, vcenter=s[1], vmax=s.values.max())
    return ['background-color: {:s}'.format(matplotlib.colors.to_hex(c.flatten())) for c in cmap(norm(s.values))]

styles = [
    dict(selector="tr:hover",
                props=[("background", "#f4f4f4")]),
    dict(selector="th", props=[("color", "#fff"),
                               ("border", "1px solid #eee"),
                               ("padding", "10px 20px"),
                               ("border-collapse", "collapse"),
                               ("background", "#17408B"),
                               ("text-transform", "uppercase"),
                               ("font-size", "13px")
                               ]),
    dict(selector="td", props=[("color", "#000000"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("font-size", "15px")
                               ]),
    dict(selector="table", props=[
                                    ("font-family" , 'Arial'),
                                    ("margin" , "25px auto"),
                                    ("border-collapse" , "collapse"),
                                    ("border" , "1px solid #eee"),
                                    ("border-bottom" , "2px solid #00cccc"),                                    
                                      ]),
    dict(selector="caption", props=[("caption-side", "bottom")])
]

ComparingList = [ ]

bestlist = ["Stephen Curry", "Zach LaVine", "Donovan Mitchell"]

def comparemultiple(listofnames):
    listofstats = getplayersstats(listofnames)
    if listofstats[0].position == "G":
        ComparingList.append(ListOfStatPositions[1])
        ComparingList.extend(listofstats)
        ComparingList.append(ListOfStatPositions[0])
        print(ComparingList) 
    elif listofstats[0].position == "F":
        ComparingList.append(ListOfStatPositions[2])
        ComparingList.extend(listofstats)
        ComparingList.append(ListOfStatPositions[0])
        print(ComparingList)
    elif listofstats[0].position == "C":
        ComparingList.append(ListOfStatPositions[3])
        ComparingList.extend(listofstats)
        ComparingList.append(ListOfStatPositions[0])
        print(ComparingList)
    df = pd.DataFrame.from_records([x.as_dict() for x in ComparingList])
    html = df.style.set_table_styles(styles).apply(background_with_norm, subset = pd.IndexSlice[0:len(listofnames),["Three Pointers Made",  "Fieldgoal Percentage", "Freethrow Percentage", "Rebounds","Assists",
    #"Turnovers",
    "Steals", "Blocks","Points"]]).apply(background_with_normto, subset = pd.IndexSlice[0:len(listofnames),["Turnovers"]]).to_html()
    text_file = open("playercomparetable.html", "w")
    text_file.write(html)
    text_file.close()
    print(df)


comparemultiple(bestlist)



