import os,sys
from datetime import datetime
from thyroid.logger import logging
from thyroid.exception import ThyroidException
FILE_NAME = "thyroid.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainingPipelineConfig:
    def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(),'artifact', f"{datetime.now().strftime('%m%d%Y___%M%H%S')}")


class DataIngestionConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        try:
            logging.info('We are in data ingestion')
            self.database_name = "thyroid"
            self.collection_name = "data"
            self.test_size =0.2
            logging.info('artifact directory is being created')
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            logging.info('feature store is being created')
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store", FILE_NAME)
            logging.info('Train and Test separated CSV file being created')
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
        except Exception as e:
            raise ThyroidException(e,sys)

    def to_dict(self,)->dict:
        try:
            return self.__dict__

        except Exception as e:
            raise ThyroidException(e,sys)

class DataValidationConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir,"data_validation")
        self.report_file_path = os.path.join(self.data_validation_dir,'report.yaml')
        





class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...