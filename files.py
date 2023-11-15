from csv_creation import folder_walk, process_csv_files
#from csv_creation import folder_walk, process_csv_files
import os
import pandas as pd
from src.constants import constants
import shutil

data_folder = constants.DATA_FOLDER
os.makedirs(data_folder, exist_ok=True)
column_names = ["time", "avg_rss12", "var_rss12", "avg_rss13", "var_rss13", "avg_rss23", "var_rss23"]

def files():
    folder_original_path = folder_walk()
    for subfolder in os.listdir(folder_original_path):
        subfolder_path = os.path.join(folder_original_path, subfolder)
        if os.path.isdir(subfolder_path):
            datasets = process_csv_files(subfolder)
    df = pd.concat(datasets, ignore_index=True)
    df.to_csv("exercise_data.csv")
    moved = shutil.move(os.path.join(os.getcwd(), 'exercise_data.csv'), os.path.join(os.getcwd(), data_folder))
    if moved:
        print("CSV FILE SUCCESSFULLY MOVED TO DATA_FOLDER")
    else:
        print("CSV FILE NOT MOVED")
    return df



if __name__ == "__main__":
    files()
        
