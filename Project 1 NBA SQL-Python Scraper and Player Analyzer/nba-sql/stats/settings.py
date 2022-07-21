import os
from dotenv import load_dotenv
load_dotenv()
from peewee import *

DB_NAME = 'nba_stats'
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'password123!' # this is your password

#used to specify database in later scripts
class Settings:
    def __init__(self):
        self.db = MySQLDatabase(
        DB_NAME,
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        charset='utf8mb4'
        )
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36'



