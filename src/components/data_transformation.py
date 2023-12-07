import sys 
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.excecption import CustomExcecption
from src.logger import logging
import os


class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")             # TO STORE MODELS AS PICKEL FILE


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig(

        )

    def get_data_transforrmer_object(self):
        """
        this function is risponsible fo data transformation
        """
        try:
            numerical_columns=['reading_score', 'writing_score']
            categorical_columns= ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),           #Handeling missing values
                    ("scaler",StandardScaler())
                ]
            )
            logging.info("Numerical columns standard scaling completed")
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler())
                ]

            )
            logging.info("Categorical columns encoding completed")

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipelines",cat_pipeline,categorical_columns)
                ]

            )
            return preprocessor
        

        except Exception as e:
            raise CustomExcecption(e,sys)
