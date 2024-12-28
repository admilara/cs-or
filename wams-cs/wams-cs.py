# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 20:59:01 2024

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



mypath = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\wams-cs"""
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in files:
    print(file)
    
savepath = r"""C:\Users\larab\Documents\GitHub\admilara.github.io\wams-cs"""

dfs = []

fdict = {"24-12-03-1044_to_24-12-03-1120_v2.1.2975.xlsx": {"search_strings": ["Phasor", "PMU#318"],
                                                          "start": "2024-12-04 09:12:58",
                                                          "end": "2024-12-04 10:20:29",
                                                          "unit": "A",
                                                          "PMUS": 1},
         "24-12-03-1306_to_24-12-03-1403_v2.1.2975.xlsx": {"search_strings": ["Phasor", "PMU#318", "PMU#323"],
                                                          "start": "2024-12-04 11:48:26",
                                                          "end": "2024-12-04 12:46:48",
                                                          "unit": "D",
                                                          "PMUS": 2}}