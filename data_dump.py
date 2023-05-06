import pymongo
import pandas as pd
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
import json
DATABASE_NAME = "thyroid"
COLECTION_NAME = "data"

if __name__ =="__main__":
    df = pd.read_csv("/config/workspace/dataset/allrep.data",header = None)
    column_list = ['age',
        'sex',
        'on_thyroxine',
        'query_on_thyroxine',
        'on_antithyroid_medication',
        'sick',
        'pregnant',
        'thyroid_surgery',
        'I131_treatment',
        'query_hypothyroid',
        'query_hyperthyroid',
        'lithium',
        'goitre',
        'tumor',
        'hypopituitary',
        'psych',
        'TSH_measured',
        'TSH',
        'T3_measured',
        'T3',
        'TT4_measured',
        'TT4',
        'T4U_measured',
        'T4U',
        'FTI_measured',
        'FTI',
        'TBG_measured',
        'TBG',
        'referral_source',
        'Class']
    
    df.columns = column_list
    print(f"Rows and columns: {df.shape}")


    #reseting the index
    df.reset_index(drop=True, inplace = True)

    #converting dataframe to json
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[:2])

    #insert convereted json record to mongo db
    client[DATABASE_NAME][COLECTION_NAME].insert_many(json_record)

