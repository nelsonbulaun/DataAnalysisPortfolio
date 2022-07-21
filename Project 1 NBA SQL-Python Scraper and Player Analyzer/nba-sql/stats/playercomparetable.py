from __future__ import print_function
from audioop import avg
import pymysql
import pandas as pd

from getaveragestats import PlPosition
from getaveragestats import ListOfStatPositions
from getplayerstats import getplayerstats


def playercomparetable(zname):
    z = getplayerstats(zname)
    ComparingList = [
    z, 
    ListOfStatPositions[0],
    ListOfStatPositions[1],
    ListOfStatPositions[2],
    ListOfStatPositions[3]]
    df = pd.DataFrame.from_records([x.as_dict() for x in ComparingList])
    print(df)

#playercomparetable("Stephen Curry")
 

