from src.exception import CustomException
import os, sys
from src.logger import logging
from zipfile import ZipFile


def extract_folder(file_path:str, folder_path=None):
    try:
        with ZipFile(file_path, 'r') as zObject:
            if folder_path is not None:
                zObject.extractall(folder_path)
            else:
                zObject.extract()
            return folder_path if folder_path else os.getcwd()
    except Exception as e:
        logging.info("An error has occured")
        raise CustomException(e, sys)
    


