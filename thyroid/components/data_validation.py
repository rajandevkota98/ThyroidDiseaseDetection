from thyroid import utils
from thyroid.entity import config_entity
from thyroid.entity import artifact_entity
from thyroid.exception import ThyroidException
from thyroid.logger import logging
import pandas as pd
from typing import Optional 
from scipy.stats import ks_2samp

class DataValidation:

    def __init__(self, data_validation_config:config_entity.DataValidationConfig):
        try:
            logging.info('Data Validation Starts')
            self.data_validation_config =data_validation_config
            self.Validation_error = dict()
        except Exception as e:
            raise ThyroidException(e,sys)



    def drop_missing_valye_columns(self,df: pd.DataFrame,threshold=0.3)->Optional[pd.DataFrame]
        try:
            null_report = df.isna().sum()/df.shape[0]
            drop_column_names = null_report[null_report>threshold].index

            self.Validation_error["dropped_column"] = drop_column_names
            df.drop(list(drop_column_names),axis=1,inplace=True)
            #return none if no columns left
            if len(df.columns)==0:
                return None
            return df
        except Exception as e:
            raise SensorException(e,sys)


    def is_required_columns_exists(self,base_df: pd.DataFrame, current_df: pd.DataFrame)->bool:
        try:
             base_columns = base_df.base_columns
             current_columns = current_df.columns
             missing_columns = []

            for base_column in base_columns:
                if base_column not in current_columns:
                    missing_columns.append(base_column)

            if len(missing_columns)>0:
                self.Validation_error['missing columns'] = missing_columns  

        except Exception as e:
            raise SensorException(e,sys)



    def data_drift(self, base_df:pd.DataFrame, current_df: pd.DataFrame):
        try:
            base_columns = base_df.columns
            current_df = current_df.columns

            for base_column in base_columns:
                base_data, current_data = base_df[base_column],current_df[base_column]
                same_distribution = ks_2samp(base_data,current_data)

                if same_distribution.pvalue>0.05:
                    pass
                    #same distribution
                else:
                    pass
                    #distribution different
                
                    



        except Exception as e:
            raise SensorException(e,sys)

    def initiate_data_validation(self,):
        pass