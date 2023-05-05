import pandas as pd 
from thyroid.config import mongo_client
from thyroid.exception import ThyroidException
from thyroid.logger import logging 
import os,sys


def get_collection_as_dataframe(database_name:str, collection_name:str)->pd.DataFrame:
    """
    This function returns collection as dataframe 
    """


    try:
        logging.info('Reading data from Database')
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"The data frame is created of {df.shape} shape")
        logging.info(f"The columns name are {df.columns}")
        if "_id" in df.columns:
            logging.info('Droping the _id  column form the dataframe')
            df = df.drop('_id', axis=1)
        return df
    except Exception as e:
        raise ThyroidException(e,sys)




