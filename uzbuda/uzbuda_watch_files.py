# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 15:01:03 2025

@author: Lara Buljan
"""

import pandas as pd
import re
from os import listdir
from os.path import isfile, join

from datetime import datetime
from datetime import timedelta

import plotly
import plotly.graph_objects as go
import plotly.io as pio

def draw(table_df, signal_name, signal_data):    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=table_df["Datetime"],
        y=table_df[signal_name],
        mode="lines",
        name=signal_data['label'] + " [" + signal_data['unit']+ "]",
        line=dict(color="blue")
        ))
        
    fig.update_layout(
        title=f"{signal_data['longtxt']}",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True,
                   title=signal_data['label'] + " [" + signal_data['unit']+ "]",
                   titlefont=dict(color="blue"),
                   tickfont=dict(color="blue"))
        )
    return fig

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

savepath = r"""C:\Users\larab\Documents\GitHub\admilara.github.io\uzbuda"""
datapath_cs = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\INEM\Zakucac_snimke\Crni_start"""
datapath_or = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\INEM\Zakucac_snimke\Otocni_rad"""

gens = ["Generator A", "Generator B", "Generator C", "Generator D"]

signali = {
    'VGACTINV': {
        'intbase': 23405,
        'baseval': 16.0,
        'unit': 'kV',
        'label': 'Ug',
        'longtxt': 'Napon generatora'},
    'VGACT': {
        'intbase': -23405,
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
        'intbase': 1.0,
        'baseval': 1.0,
        'unit': 'logički signal',
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
        'longtxt': 'Referenca Ug'},
    'QCONRON1': {
        'intbase': 1.0,
        'baseval': 1.0,
        'unit': 'logički signal',
        'label': 'Q reg on',
        'longtxt': 'Q regulator ukljucen'
        },
    'QCONROF1': {
        'intbase': 1.0,
        'baseval': 1.0,
        'unit': 'logički signal',
        'label': 'Q reg off',
        'longtxt': 'Q regulator iskljucen'
        },
    'FGACT': {
        'intbase': 11703,
        'baseval': 50.0,
        'unit': 'Hz',
        'label': 'f',
        'longtxt': 'Frekvencija'
        },
    'VRINC': {
        'intbase': 23405,
        'baseval': 1.0,
        'unit': 'pu',
        'label': 'Vref NIŽE',
        'longtxt': 'Impuls Vref niže'},
    'VRDEC': {
        'intbase': 23405,
        'baseval': 1.0,
        'unit': 'pu',
        'label': 'Vref VIŠE',
        'longtxt': 'Impuls Vref više'}
    }

# =============================================================================
#                           START - WATCH
# =============================================================================


all_watch_files = []
for gen in gens:
    datapath = datapath_cs + "\\" + gen + "\\"
    files_cs = [f for f in listdir(datapath) if isfile(join(datapath, f))]
    
    datapath = datapath_or + "\\" + gen + "\\"
    files_or = [f for f in listdir(datapath) if isfile(join(datapath, f))]


    for file in files_cs:
        if 'RecEx' in file:
            continue
        else:
            path = datapath_cs + "\\" + gen + "\\" + file
            all_watch_files.append(['CS', gen, path])
            
    for file in files_or:
        if 'RecEx' in file:
            continue
        else:
            path = datapath_or + "\\" + gen + "\\" + file
            all_watch_files.append(['OR', gen, path])            

    #file = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\INEM\Zakucac_snimke\Crni_start\Generator A\RecEx_ZAKUCA1A_003.log"""
    #file_name = "RecEx_ZAKUCA1A_003"

# =============================================================================
#                   READ HEADER - WATCH FILES
# =============================================================================
# Header file - samo date i time su bitni, Watch fileovi nemaju toliko puno
# informacija u tekstu kao što imaju RecEx fileovi.

for file_set in all_watch_files:
    file = file_set[-1]
    file_name = file.split("\\")[-1]
    #print(file_name)

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
#               READ WATCH FILES - SIGNALS & DATA
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
    
    # print("\n")
    # Display results
    # print("Signals:")
    # for signal in signals:
    #     print(f"{signal[0]} ({signal[1]})")
     
    # print("\nDataFrame:")
    # print(df)

    #print("\nHeader info:")
    #print(header_info)
    
    datetime_str = header_info['datetime']
    datetime_start = datetime.strptime(datetime_str, '%d.%m.%Y. %H:%M:%S')
    #dt = timedelta(milliseconds = int(sample_data["Sample Time"]))
    df['Timedelta'] = pd.to_timedelta(df['Time'], unit='s')
    
    df["Datetime"] = datetime_start + df["Timedelta"]

    
#TODO - TURN TO BASE VALUES

    column_skip = ['Time', 'Timedelta', 'Datetime', 'DEINVERT', 'ACKGPON1']
    column_list = [column for column in df.columns if column not in column_skip]
    #print(column_list)
    table_df = pd.DataFrame()
    table_df["Datetime"] = df["Datetime"]

    for column in column_list:
        if column == 'DEINVERT':
            continue
        
        column_data = signali[column]
        table_df[column] = df[column]/column_data['intbase']
        table_df[column] = table_df[column]*column_data['baseval']    

#TODO - DRAW FIGS

    fig_list = []
    for column in column_list:
        fig = draw(table_df, column, signali[column])
        fig_list.append(fig)

    html_list = []
    for index,fig in enumerate(fig_list):
        if index == 0:
            html = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
        else:
            html = pio.to_html(fig, full_html=False, include_plotlyjs=False)
        html_list.append(html)

    divs_html = "\n".join(f"<div>{html}</div>" for html in html_list)
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{file_name}</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    </head>
    <body>
        <h3>{gen} {file_set[0]} - {file_name}</h3>
        {divs_html}
        </body>
    </html>
    """
    
    if file_set[0] == "CS":
        with open(f"{savepath}\\WATCH\\CS\\{file_name.lower()}.html", "w") as file:
            file.write(html_content)
    else:
        with open(f"{savepath}\\WATCH\\OR\\{file_name.lower()}.html", "w") as file:
            file.write(html_content)    

    print(file_set[0])
    print(file_name)
    print(table_df.iloc[0]["Datetime"])
    print(table_df.iloc[-1]["Datetime"])
    print(table_df.iloc[-1]["Datetime"] - table_df.iloc[0]["Datetime"])
    print("\n")
