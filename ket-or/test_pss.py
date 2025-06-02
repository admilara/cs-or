# -*- coding: utf-8 -*-
"""
Created on Thu May 29 12:45:06 2025

@author: Lara Buljan
"""

import re
import pandas as pd


pss_path = "C:/Users/larab/Documents/GitHub/cs-or/cs-or/wams-or/pss-on-off.txt"

# Read and split by line
with open(pss_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Parse lines using regex
parsed_data = []
pattern = re.compile(r"(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}:\d{3})\s+(?P<plant>HE ZAK)\s+(?P<voltage>\d+)\s+(?P<generator>GENER\d+)\s+UZBUDA PSS UKJLJUČEN\s+(?P<status>PRORADA|PRESTANAK)")

for line in lines:
    match = pattern.match(line.strip())
    if match:
        parsed_data.append(match.groupdict())

# Create DataFrame
df = pd.DataFrame(parsed_data)

# Convert datetime to pandas datetime
df['datetime'] = pd.to_datetime(df['datetime'], format="%Y-%m-%d %H:%M:%S:%f")

df = df.drop(columns=["plant", "voltage"])

generator_map = {
    'GENER1': 'A',
    'GENER2': 'B',
    'GENER3': 'C',
    'GENER4': 'D'
}
df['generator'] = df['generator'].replace(generator_map)

# Replace status values
status_map = {
    'PRESTANAK': 'PSS OFF',
    'PRORADA': 'PSS ON'
}
df['status'] = df['status'].replace(status_map)

