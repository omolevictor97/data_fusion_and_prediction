import os, sys
from extract_file import extract_folder
from src.exception import CustomException
from src.logger import logging
from src.constants import constants
import pandas as pd
import shutil


FILE_TO_EXTRACT_FROM_PATH= constants.FILE_TO_EXTRACT_PATH
FOLDER_PATH = constants.FOLDER_PATH
column_names = ["time", "avg_rss12", "var_rss12", "avg_rss13", "var_rss13", "avg_rss23", "var_rss23"]
columns_len = 5
# Define the path to your replacement line (if needed)
replacement_line_path = "replacement_line.txt"

def folder_walk():
    try:
        file_path = os.path.join(os.getcwd(), FILE_TO_EXTRACT_FROM_PATH)
        folder_path = os.path.join(os.getcwd(), FOLDER_PATH)
        folder_original_path = extract_folder(file_path=file_path, folder_path=folder_path)
        return folder_original_path
    except Exception as e:
        logging.info("Error occured in folder_walk function")
        raise CustomException(e, sys)
    

"""def root_folder():
    try:
        root_folder = folder_walk()
        return root_folder
    except Exception as e:
        logging.info("Error Occured Inside root folder file")
        raise CustomException(e, sys)"""



def process_csv_files(subfolder):
    try:
        root_path = folder_walk()
        dataframes = []
        #sub_folder_path = os.path.join(root_path, subfolder)
        for root, dir, files in os.walk(root_path):
            
            for file in files:
                
                if file.endswith(".csv"):
                    folder_name = os.path.basename(root)
                    #print(folder_name)
                    file_path = os.path.join(root, file)
                    df = pd.read_csv(f"{file_path}", on_bad_lines='skip', skiprows=5, names= column_names)
                    df["Label"] = folder_name
                    dataframes.append(df)
        return dataframes
    except Exception as e:
        logging.info("Error has occured in process_csv_files function")
        raise CustomException(e, sys)
    




