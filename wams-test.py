# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 12:13:21 2024

@author: larab
"""
import plotly
import plotly.graph_objects as go
import plotly.io as pio
from datetime import timedelta

from os import listdir
from os.path import isfile, join

import pandas as pd
import numpy as np

from scipy.interpolate import UnivariateSpline, interp1d

mypath = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\wams-or"""
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

dfs = []

fdict = {"24-12-04-0812_to_24-12-04-0921_v2.1.2975.csv": {"search_strings": ["Phasor", "PMU#318"],
                                                          "start": "2024-12-04 09:12:58",
                                                          "end": "2024-12-04 10:20:29",
                                                          "unit": "A",
                                                          "PMUS": 1},
         "24-12-04-1048_to_24-12-04-1147_v2.1.2975.csv": {"search_strings": ["Phasor", "PMU#318", "PMU#323"],
                                                          "start": "2024-12-04 11:48:26",
                                                          "end": "2024-12-04 12:46:48",
                                                          "unit": "D",
                                                          "PMUS": 2},
         "24-12-04-1324_to_24-12-04-1426_v2.1.2975.csv": {"search_strings": ["Phasor", "PMU#318", "PMU#324"],
                                                          "start": "2024-12-04 14:24:28",
                                                          "end": "2024-12-04 17:03:18",
                                                          "unit": "B",
                                                          "PMUS": 2},
         "24-12-04-1527_to_24-12-04-1603_v2.1.2975.csv": {"search_strings": ["Phasor", "PMU#318"], 
                                                          "start": "2024-12-04 16:27:27", 
                                                          "end": "2024-12-04 17:03:18",
                                                          "unit": "C",
                                                          "PMUS": 1}}


# =============================================================================
#                       DATAFRAMES FROM CSV FILES
# =============================================================================

col_strings = ["Phasor", "|UN| magn [pu]", "|IN| magn [A]", "f(PMU) [Hz]", "P [W]", "Q [VAr]"]
# col_strings = [string.encode("utf-8") for string in strings]

for file in files:
    print(file)
    print("\n")
    wams_df = pd.read_csv(mypath + "\\" + file, header=0, delimiter=",")
    wams_df["PhasorDatetime"] = (wams_df["PhasorDate"] + ' ' + wams_df["PhasorTime"] + "." + wams_df["PhasorMs"].astype(str))
    wams_df['PhasorDatetime'] = pd.to_datetime(wams_df['PhasorDatetime'], format='%Y-%m-%d %H:%M:%S.%f')
    wams_df['PhasorDatetime'] = wams_df["PhasorDatetime"] + timedelta(hours=1)
    
    search_strings = fdict[file]["search_strings"]
    
    filtered_wams_df = wams_df[[col for col in wams_df.columns if any(s in col for s in search_strings)]]
    filtered_wams_df = filtered_wams_df[[col for col in filtered_wams_df.columns if any(s in col for s in col_strings)]]
    fdict[file]["df"] = filtered_wams_df
    

for key, value in fdict.items():
    for i in range(value["PMUS"]):
        print(i)
    
    
    
        
    
    


