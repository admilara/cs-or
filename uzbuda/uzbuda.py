# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:19:35 2025

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

def extract_sample_and_trigger_times(lines):
    # Combine lines into a single string for regex processing
    log_text = ''.join(lines)
    
    # Define patterns for sample time and trigger time
    sample_time_pattern = r"Sample time:\s+(\d+)"
    trigger_time_pattern = r"Trigger time:\s+([\d.]+\s[\d:.]+)"
    trigger_position_pattern = r"Trigger position:\s+(\d+) @([\w\d]+)"


    # Search the log text for the patterns
    sample_time_match = re.search(sample_time_pattern, log_text)
    trigger_time_match = re.search(trigger_time_pattern, log_text)
    trigger_position_match = re.search(trigger_position_pattern, log_text)


    # Extract values from matches
    sample_time = int(sample_time_match.group(1)) if sample_time_match else None
    trigger_time = trigger_time_match.group(1) if trigger_time_match else None
    trigger_position = (
        {
            "position": int(trigger_position_match.group(1)),
            "hex": trigger_position_match.group(2),
        }
        if trigger_position_match
        else None
    )

    # Return as a dictionary
    return {
        "Sample Time": sample_time,
        "Trigger Time": trigger_time,
        "Trigger Position": trigger_position,
    }


def extract_signals(lines):   
    extracted = []
    signal_pattern = r"\s*(\d+)\.\s+([\w:]+):\s+([\w.]+)"
    for line in lines:
        if line.startswith("Connected signals:"):
            num_signals = int(line.split(":")[1].strip())
        if re.match(signal_pattern, line):
            match = re.match(signal_pattern, line)
            extracted.append(match.groups())
        if line.startswith("Sample time:"):
            break
    return extracted

def extract_header_data(lines):
    extracted = {}
    header_pattern = r"(.*?):\s*(.*)"
    for line in lines:
        match = re.match(header_pattern, line)
        if match:
            key, value = match.groups()
            extracted[key.strip()] = value.strip()
        if line.startswith("Connected signals:"):
            break
    return extracted

def extract_table_data(lines):
    table_start = False
    table_lines = []
    for line in lines:
        if re.match(r"\s*Addr", line):
            table_start = True
            continue
        if table_start:
            if not line.strip():
                break
            table_lines.append(line.strip())

    # Convert table data into a DataFrame
    extracted = []
    for line in table_lines:
        row = re.split(r"\s+", line)
        extracted.append(row)
    return extracted

def draw(table_df, signal_name, signal_data, trigger_time):    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=table_df["Datetime"],
        y=table_df[signal_name],
        mode="lines",
        name=signal_data['label'] + " [" + signal_data['unit']+ "]",
        line=dict(color="blue")
        ))
    
    fig.add_vline(
        x=trigger_time,
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )
    
    fig.add_annotation(
        x=trigger_time,
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"TRIGGER TIME: {trigger_time}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="red", size=12),
        bordercolor="red",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    
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
        }
    }



# =============================================================================
#                           START - RECEX
# =============================================================================

all_recex_files = []
for gen in gens:
    datapath = datapath_cs + "\\" + gen + "\\"
    files_cs = [f for f in listdir(datapath) if isfile(join(datapath, f))]
    
    datapath = datapath_or + "\\" + gen + "\\"
    files_or = [f for f in listdir(datapath) if isfile(join(datapath, f))]


    for file in files_cs:
        if 'Watch' in file:
            continue
        else:
            path = datapath_cs + "\\" + gen + "\\" + file
            all_recex_files.append(['CS', path])
            
    for file in files_or:
        if 'Watch' in file:
            continue
        else:
            path = datapath_or + "\\" + gen + "\\" + file
            all_recex_files.append(['OR', path])            

    #file = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\INEM\Zakucac_snimke\Crni_start\Generator A\RecEx_ZAKUCA1A_003.log"""
    #file_name = "RecEx_ZAKUCA1A_003"

# =============================================================================
#                           READ RECEX FILES
# =============================================================================

for file_set in all_recex_files:
    file = file_set[1]
    # Read the log file
    file_name = file.split("\\")[-1]
    with open(file, "r") as file:
        lines = file.readlines()
    
    # Extract header data
    header_data = extract_header_data(lines)
    
    # Locate and parse signal data
    signals = extract_signals(lines)
    
    signals_df = pd.DataFrame(signals, columns=["Index", "Address", "Signal"])
    
    # Extract table data
    table_data = extract_table_data(lines)
    
    # Extract column names and data -> create DataFrame from the table_data
    columns = ["Addr"] + [signals_df.iloc[i]["Signal"] for i in range(len(signals_df["Signal"]))]
    table_df = pd.DataFrame(table_data, columns=columns)
    
    # Clean up the DataFrame
    table_df.iloc[:, 1:] = table_df.iloc[:, 1:].apply(pd.to_numeric)
    
    # Extract sample timestep and start of record
    sample_data = extract_sample_and_trigger_times(lines)
    
    # Output results
    #print("Header Data:")
    #print(header_data)
    #print("\nSignals Data:")
    #print(signals_df)
    #print("\nTable Data:")
    #print(table_df)
    #print("\nSample and trigger time:")
    #print(sample_data)


# =============================================================================
#                    ADD DATETIME OBJS TO TABLE DATA
# =============================================================================

    datetime_str = sample_data["Trigger Time"]
    datetime_start = datetime.strptime(datetime_str, '%d.%m.%Y. %H:%M:%S.%f')
    dt = timedelta(milliseconds = int(sample_data["Sample Time"]))
    
    table_df["Datetime"] = None 
    
    trigger_index = sample_data["Trigger Position"]['position'] - 1
    
    table_df.at[trigger_index, "Datetime"] = datetime_start
    
    for i in range(trigger_index - 1, -1, -1):
        table_df.at[i, "Datetime"] = table_df.at[i+1, "Datetime"] - dt
    
    for i in range(trigger_index + 1, len(table_df)):
        table_df.at[i, "Datetime"] = table_df.at[i-1, "Datetime"] + dt
 

# =============================================================================
#                        RECALCULATE VALUES TO BASE
# =============================================================================

# Preračun na bazne vrijednosti
# Vrijednosti su dane u odnosu na IntBase vrijednost signala
# Svaki signal ima svoju IntBase vrijednost i svoju BaseVal, vrijednost koja je 
# razumljiva u kontekstu tih veličina, dakle V, A, pu, MW, Mvar itd.
# Dictionary signali drzi sve vrijednosti kako su one nazvane u RecEx fileu, 
# njihove intbase vrijednosti, baseval vrijednosti, mjerne jedinice i nazive
# signali = {'recex_ime': {'intbase':
#                           'baseval':
#                           'unit': 
#                           'label':
#                           'longtxt': }}


    column_skip = ['Addr', 'Datetime', 'DEINVERT', 'ACKGPON1']
    column_list = [column for column in table_df.columns if column not in column_skip]
    # print(column_list)
    table_df_values = pd.DataFrame()
    table_df_values["Addr"] = table_df["Addr"]
    table_df_values["Datetime"] = table_df["Datetime"]
    
    for column in column_list:
        if column == 'DEINVERT':
            continue
    
        column_data = signali[column]
        table_df_values[column] = table_df[column]/column_data['intbase']
        table_df_values[column] = table_df_values[column]*column_data['baseval']


# =============================================================================
#                   DRAW FIGS                    
# =============================================================================

    fig_list = []
    for column in column_list:
        fig = draw(table_df_values, column, signali[column], datetime_start)
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
        with open(f"{savepath}\\CS\\{file_name.lower()}.html", "w") as file:
            file.write(html_content)
    else:
        with open(f"{savepath}\\OR\\{file_name.lower()}.html", "w") as file:
            file.write(html_content)
    print(file_set[0])
    print(file_name)
    print(table_df_values.iloc[0]["Datetime"])
    print(table_df_values.iloc[-1]["Datetime"])
    print(table_df_values.iloc[-1]["Datetime"] - table_df_values.iloc[0]["Datetime"])
    print("\n")



