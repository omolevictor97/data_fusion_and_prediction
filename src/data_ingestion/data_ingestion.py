import os, sys
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
import pandas as pd


@dataclass

class DataIngestionConfig:
    # Create the raw data, train data and test data path

    raw_data_path:str = os.path.join("artifacts", "raw.csv")
    train_data_path:str = os.path.join("artifacts", "train.csv")
    test_data_path:str = os.path.join("artifacts", "test.csv")

##### Creating the data ingestion class

class DataIngestion:

    def __init__(self):
        # Initializing data ingestion
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Start From Here")

        try:
            df = pd.read_csv(os.path.join("data_folder", "exercise_data.csv"))
            data= df.copy()
            data = data.dropna()
            logging.info("Dataframe has been read successfully")
            
            # we shall save the read raw_data into its file
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True) #To create the raw data folder
            data.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # After getting the dataframe read and saved in its container/folder, we shall split the data into train and test
            #dataset

            logging.info("Train and Test data split")

            train_set, test_set = train_test_split(data, test_size=0.1, random_state=42)

            # Save the train and test data set into their respective containers/folders
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Train test split completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

            return 
        except Exception as e:
            logging.info("An Error has occured at initiate_data_ingestion at DataIngestion class")
            raise CustomException(e,sys)

    
