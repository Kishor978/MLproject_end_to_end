import os
import sys
from src.excecption import CustomExcecption
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:              #for providing inputs as path
    train_test_path: str=os.path.join('artifacts','train.csv')    #path to save output for training data
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()     # path will be stored in veriable

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or componemt")
        try:
            df=pd.read_csv('E:\MLprojet\notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_test_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
        except: 
            pass