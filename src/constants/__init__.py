import os,sys
from datetime import datetime

def get_currrent_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

CURRENT_TIME_STAMP=get_currrent_time_stamp()

ROOt_DIR_KEY=os.getcwd()
DATA_DIR="Data"
DATA_DIR_KEY="finalTrain.csv"

ARTIFACT_DIR_KEY="Artifact"

#data ingestion related variable--------------------------------

DATA_INGESTIOn_KEY="data_ingestion"
DATA_INGESTION_RAW_DATA_DIR="raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_KEY="ingested_dir"

RAW_DATA_DIR_KEY="raw.csv"
TRAIN_DATA_DIR_KEY="train.csv"
TEST_DATA_DIR_KEY="test.csv"

# data transformation related variable--------------------

# artifact / data_transformation / procceor->processor.pkl and transformation -> train.csv and test.csv\
#procceor->processor.pkl
#transformation -> train.csv and test.csv
DATA_TRANSFORMATION_ARTIFACT = "data_transformation"
DATA_PREPROCCED_DIR = "procceor"
DATA_TRANSFORMTION_PROCESSING_OBJ = "processor.pkl"
DATA_TRANSFORM_DIR = "transformation"
TRANSFORM_TRAIN_DIR_KEY = "train.csv"
TRANSFORM_TEST_DIR_KEY = "test.csv"


#model training variable-------------------------------
MODEL_TRAINER_KEY="model_trainer"
MODEL_OBJECT="model.pkl"


