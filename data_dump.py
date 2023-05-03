import pymongo
import pandas as pd
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
import json
DATABASE_NAME = "thyoroid"
COLECTION_NAME = "data"

if __name__ =="__main__":
    df = pd.read_csv("/config/workspace/dataset/thyroid0387.csv")
    print(f"Rows and columns: {df.shape}")


    #reseting the index
    df.reset_index(drop=True, inplace = True)

    #converting dataframe to json
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[:2])

    #insert convereted json record to mongo db
    client[DATABASE_NAME][COLECTION_NAME].insert_many(json_record)

