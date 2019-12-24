# -*- coding: utf-8 -*-
"""
2019
@author: wuffalo
"""

import pandas as pd
import os

path_to_SOS = "/mnt/shared-drive/05 - Office/FTP/FTP Files/"

file_list = []

for subdir, dirs, files in os.walk(path_to_SOS):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".xlsx"):
            if filepath not in file_list:
                file_list.append(filepath)

df_list = []

# for each file name, grab file, format and append to list of dataframes
for f in file_list:
    sheet = pd.read_excel(f)
    df_list.append(sheet)

Master_SOS = pd.concat(df_list, ignore_index=True, sort=False)

Master_SOS.to_feather('C:/Users/WMINSKEY/Output/Master_SOS.file',index=False)