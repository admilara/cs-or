# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 15:01:03 2025

@author: Lara Buljan
"""

import pandas as pd
import re
from os import listdir
from os.path import isfile, join

def extract_signals(lines):
    signals = []
    signals_start = False
    for line in lines:
        if line.startswith("Signals:"):
            signals_start = True
        elif signals_start and re.match(r"\d+\.\s", line.strip()):
            match = re.match(r"\d+\.\s+(\S+)\s+(\S+)", line.strip())
            if match:
                signal_name, signal_type = match.groups()
                signals.append((signal_name, signal_type))
        elif signals_start and not line.strip():
            break
    return signals

# Step 2: Extract the Data
def extract_data(lines):
    data = []
    data_start = False
    for line in lines:
        if line.startswith("Data:"):
            data_start = True
        elif data_start and line.strip():
            data.append(line.strip())
    return data


datapath_cs = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\INEM\Zakucac_snimke\Crni_start"""
datapath_or = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\INEM\Zakucac_snimke\Otocni_rad"""

gens = ["Generator A", "Generator B", "Generator C", "Generator D"]


# =============================================================================
#                           CRNI START - RECEX
# =============================================================================

for gen in gens:
    datapath = datapath_cs + "\\" + gen + "\\"
    files_cs = [f for f in listdir(datapath) if isfile(join(datapath, f))]
    print(files_cs)
    
for gen in gens:
    datapath = datapath_or + "\\" + gen + "\\"
    files_or = [f for f in listdir(datapath) if isfile(join(datapath, f))]
    print(files_or)

signali = {
    'VGACTINV': {
        'intbase': 23405,
        'baseval': 16.0,
        'unit': 'kV',
        'label': 'Ug',
        'longtxt': 'Napon generatora'},
    'IGACTINV': {
        'intbase': 16384,
        'baseval': 5774.0,
        'unit': 'A',
        'label': 'Ig',
        'longtxt': 'Struja generatora'},
    'UFACT': {
        'intbase': 4096,
        'baseval': 74.0,
        'unit': 'V',
        'label': 'Uf',
        'longtxt': 'Napon uzbude'},
    'IFACT': {
        'intbase': 4096,
        'baseval': 725.0,
        'unit': 'A',
        'label': 'If',
        'longtxt': 'Struja uzbude'},
    'IGACT': {
        'intbase': -16384,
        'baseval': 5774.0,
        'unit': 'A',
        'label': 'Ig',
        'longtxt': 'Struja generatora'},
    'PACT': {
        'intbase': 23405,
        'baseval': 160.0,
        'unit': 'MW',
        'label': 'Pg',
        'longtxt': 'Radna snaga generatora'},
    'QACT': {
        'intbase': 23405,
        'baseval': 160.0,
        'unit': 'Mvar',
        'label': 'Qg',
        'longtxt': 'Jalova snaga generatora'},
    'DEINVERT': {
        'intbase':0,
        'baseval':0,
        'unit': 'pu',
        'label': 'DEINVERT',
        'longtxt':'DEINVERT'},
    'ACKGBON1': {
        'intbase': 23405,
        'baseval': 1.0,
        'unit': 'pu',
        'label': 'GB on',
        'longtxt': 'Uključen generatorski prekidač'},
    'REFRDEC1': {
        'intbase': 23405,
        'baseval': 1.0,
        'unit': 'pu',
        'label': 'Vref NIŽE',
        'longtxt': 'Impuls Vref niže'},
    'REFRINC1': {
        'intbase': 23405,
        'baseval': 1.0,
        'unit': 'pu',
        'label': 'Vref VIŠE',
        'longtxt': 'Impuls Vref više'},
    'VGREF': {
        'intbase': 23405,
        'baseval': 1.0,
        'unit': 'pu',
        'label': 'Ug ref',
        'longtxt': 'Referenca Ug'}
    }


file = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\INEM\Zakucac_snimke\Crni_start\Generator A\Watch_ZAKUCA1A_006.log"""

with open(file, "r") as file:
    log_lines = file.readlines()

header_info = {}
for line in log_lines:
    # Match the Start time line
    if match := re.match(r"Start time:\s+([\d.]+)\s+([\d:]+)", line):
        header_info["date"] = match.group(1)  # Extract date
        header_info["time"] = match.group(2)  # Extract time
header_info["datetime"] = header_info["date"] + " " + header_info["time"]

# =============================================================================
#               READ WATCH FILES 
# =============================================================================

# Extracted signals and data
signals = extract_signals(log_lines)
data_lines = extract_data(log_lines)

# Step 3: Convert Data to DataFrame
# Prepare column names
columns = ["Time"] + [signal[0] for signal in signals]

# Split and convert data lines to numeric values
data_lines = [line for line in data_lines if not line.strip().startswith("***")]
data = [list(map(float, re.split(r"\s+", line))) for line in data_lines]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Display results
print("Signals:")
for signal in signals:
    print(f"{signal[0]} ({signal[1]})")

print("\nDataFrame:")
print(df)

print("\nHeader info:")
print(header_info)