import os,sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

#sys.path.append('E:/FullStack_Data/MACHINE_LEARNING/PROJECTS/MLPROJECT5_modularcoding/New_ML_project_modular-coding')

from src.constants import *
from src.config.configuration import *

# from ..config import configuration##
# from .. import constants

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass  

from src.logger import logging
from src.exception import CustomException

from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path=TRAIN_FILE_PATH
    test_data_path=TEST_FILE_PATH
    raw_data_path=RAW_FILE_PATH


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            #reading the raw data from the specific folder
            df=pd.read_csv(DATASET_PATH)
            #lets create a folder
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)
            #saving raw data to the directory which we created
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False)

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion_config.train_data_path, header=True)

            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path),exist_ok=True)
            

            df.to_csv(self.data_ingestion_config.test_data_path)

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
    
            )

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.inititate_data_transformation(train_data,test_data)
    model_trainer=ModelTrainer()
    print(model_trainer.initiate_model_training(train_arr,test_arr))
    