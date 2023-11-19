import os, sys
from src.exception import CustomException
from src.logger import logging
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
from dataclasses import dataclass
from imblearn.over_sampling import SMOTE
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder

@dataclass

class DataTransformationConfig:
    preprocessor_obj_file_path:str = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:

    def __init__(self):
        self.preprocessor = DataTransformationConfig()

    def get_data_transformation():
        try:
            #get the columns to be transformed
            numerical_col = ["time","avg_rss12","var_rss12","avg_rss13","var_rss13","avg_rss23","var_rss23"]
            categorical_col = ["Label"]

            label_cat = ["bending1", "bending2", "cycling", "lying", "sitting", "standing", "walking"]
            numerical_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                    ]
            )

            categorical_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy='most_frequent')),
                    ('encoder', LabelEncoder(categories=[label_cat]))
                ]
            )

            preprocessor = ColumnTransformer(
                transformers=[
                    ("numerical_pipeline", numerical_pipeline, numerical_col),
                    ("categorical_pipeline", categorical_pipeline, categorical_col)
                ]
                )
            
            logging.info("Pipeline Completed")
            return preprocessor
        except Exception as e:
            logging.info("Error occured at the get_data_transformation function")
            return CustomException(e, sys)
        

