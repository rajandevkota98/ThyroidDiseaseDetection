import pymongo
import pandas as pd
import json
from dataclass import dataclass
import os

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")

client = 