import os, sys
from extract_file import extract_folder
from src.exception import CustomException
from src.logger import logging
from src.constants import constants
import pandas as pd


FILE_TO_EXTRACT_FROM_PATH= constants.FILE_TO_EXTRACT_PATH
FOLDER_PATH = constants.FOLDER_PATH

def folder_walk():
    try:
        file_path = os.path.join(os.get_cwd(), FILE_TO_EXTRACT_FROM_PATH)
        folder_path = os.path.join(os.get_cwd(), FOLDER_PATH)
        folder_original_path = extract_folder(file_path=file_path, folder_path=folder_path)
        return folder_original_path
    except Exception as e:
        logging.info("Error occured in folder_walk function")
        raise CustomException(e, sys)
    

def root_folder():
    try:
        root_folder = folder_walk()
        return root_folder
    except Exception as e:
        logging.info("Error Occured Inside root folder file")
        raise CustomException(e, sys)
    
def process_csv_files(subfolder):
    try:
        root_path = root_folder()
        sub_folder_path = os.path.join(root_path, subfolder)
        for filename in os.listdir(sub_folder_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(sub_folder_path, filename)
                #Read the CSV file path
                df = pd.read_csv(file_path)
                df["Label"] = subfolder
                df.to_csv(file_path, index=False)
    except Exception as e:
        logging.info("Error has occured in process_csv_files function")
        raise CustomException(e, sys)
