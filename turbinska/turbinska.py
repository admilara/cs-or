# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:00:32 2025

@author: Lara Buljan
"""

import plotly
import plotly.graph_objects as go
import plotly.io as pio
#import plotly.dashboard_objs as dashboard_objs
import IPython.display
#from IPyhton.display import Image

from os import listdir
from os.path import isfile, join

import pandas as pd 
import re

from datetime import datetime
from datetime import timedelta


# =============================================================================
#                    FOLDERS
# =============================================================================

savepath = r"""C:\Users\larab\Documents\GitHub\admilara.github.io\turbinska"""
datapath_cs = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\GEPPERT\cs"""
datapath_or = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\GEPPERT\or"""