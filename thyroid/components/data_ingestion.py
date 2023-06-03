from thyroid import utils
from thyroid.entity import config_entity
from thyroid.entity import artifact_entity
from thyroid.exception import ThyroidException
from thyroid.logger import logging
from sklearn.model_selection import train_test_split
import pandas as pd 
import os, sys
import numpy as np 

class DataIngestion:
    def __init__(self, data_ingestion_config:config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise ThyroidException(e,sys)

    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            #Exporting collection data as pandas dataframe
            logging.info('starting of the data ingestion')
            df: pd.DataFrame = utils.get_collection_as_dataframe(database_name='thyroid',collection_name='data')
            logging.info(f'The dataframe is obtained.Its shape is {df.shape}')
            #Removing the member id from the target class
            def remove_diagnosis_text(diagnosis):
                return diagnosis.split('.')[0]
            df['Class'] = df['Class'].apply(remove_diagnosis_text)
            for i in df.columns:
                for j in df[i]:
                    df[i] = df[i].replace('?', np.NaN)

            #create feature store foler
            logging.info('feature store dir is being created')
            feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir, exist_ok = True)
        
            #save data in feature store dirs
            logging.info(' thyroid data is dumped to the directory')
            df.to_csv(path_or_buf = self.data_ingestion_config.feature_store_file_path,index = False,header = True)

            #train test split
            logging.info('Train test split')
            train_df,test_df = train_test_split(df,test_size=self.data_ingestion_config.test_size)

            #create training dataset directory folder if not exists
            logging.info('creating directory of the train')
            training_dataset_dir = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(training_dataset_dir, exist_ok = True)


            #create testing dataset directory folder if not exists
            logging.info('creating directort for test')
            testing_dataset_dir = os.path.dirname(self.data_ingestion_config.test_file_path)
            os.makedirs(testing_dataset_dir, exist_ok = True)

            logging.info('train data is being dumped')
            train_df.to_csv(path_or_buf = self.data_ingestion_config.train_file_path,index = False,header = True)
            logging.info('testing data is being dumped')
            test_df.to_csv(path_or_buf = self.data_ingestion_config.test_file_path,index = False,header = True)



            #preparing artifacts
            logging.info('The artifact are being created')
            data_ingestion_artifact = artifact_entity.DataIngestionArtifact(
                feature_store_file_path= self.data_ingestion_config.feature_store_file_path,
                train_file_path = self.data_ingestion_config.train_file_path,
                test_file_path = self.data_ingestion_config.test_file_path
            )

            return data_ingestion_artifact
        except Exception as e:
            raise ThyroidException(e,sys)
        

 


