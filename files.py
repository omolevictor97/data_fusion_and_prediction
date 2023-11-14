from csv_creation import folder_walk, process_csv_files
#from csv_creation import folder_walk, process_csv_files
import os
import pandas as pd

column_names = ["time", "avg_rss12", "var_rss12", "avg_rss13", "var_rss13", "avg_rss23", "var_rss23"]

def files():
    larger_dataset = pd.DataFrame(columns=column_names)
    folder_original_path = folder_walk()
    for subfolder in os.listdir(folder_original_path):
        subfolder_path = os.path.join(folder_original_path, subfolder)
        if os.path.isdir(subfolder_path):
            datasets = process_csv_files(subfolder)
    df = pd.concat(datasets, ignore_index=True)
    df.to_csv("Exercise_data.csv")
    return df



if __name__ == "__main__":
    files()
        
