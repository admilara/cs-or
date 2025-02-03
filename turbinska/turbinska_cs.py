# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 09:45:01 2025

@author: larab
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

from io import StringIO


# =============================================================================
#                   FUNKCIJE
# =============================================================================

def draw(df, name, values, annotations):
    # Group columns by their 'longtxt'
    # name = longtxt
    # values = list of columns

    valid_columns = [col for col in values if col in df.columns]
    print(valid_columns)
    
    # mora postojati bolji način za ovo...
    if len(valid_columns) == 1:
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x = df["Datetime"],
            y = df[valid_columns[0]],
            mode = "lines",
            name = signali[valid_columns[0]]["label"] + " [" + signali[valid_columns[0]]["unit"] + "]",
            line = dict(color="blue")
            ))
          
        fig.update_layout(
            title=f"{signali[valid_columns[0]]['longtxt']}",
            template="plotly",
            legend=dict(title="Legenda",
                        indentation=10),
            xaxis=dict(showgrid=True),
            yaxis=dict(showgrid=True,
                       zeroline=True,
                       title=signali[valid_columns[0]]["label"] + " [" + signali[valid_columns[0]]["unit"]+ "]",
                       titlefont=dict(color="blue"),
                       tickfont=dict(color="blue"))
            )
    elif len(valid_columns) == 2:
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x = df["Datetime"],
            y = df[valid_columns[0]],
            mode = "lines",
            name = valid_columns[0],
            line = dict(color="blue")
            ))
        
        fig.add_trace(go.Scatter(
            x = df["Datetime"],
            y = df[valid_columns[1]],
            mode = "lines",
            name = valid_columns[1],
            line = dict(color="red"),
            yaxis="y2"
            ))
        
        fig.update_layout(
            title=f"{signali[valid_columns[0]]['longtxt']}",
            template="plotly",
            legend=dict(title="Legenda",
                        indentation=10),
            xaxis=dict(showgrid=True),
            yaxis=dict(showgrid=True,
                       zeroline=True,
                       title=signali[valid_columns[0]]["label"] + " [" + signali[valid_columns[0]]["unit"] + "]",
                       titlefont=dict(color="blue"),
                       tickfont=dict(color="blue")),
            yaxis2=dict(showgrid=True,
                        zeroline=True,
                        title=signali[valid_columns[1]]["label"] + " [" + signali[valid_columns[1]]["unit"] + "]",
                        titlefont=dict(color="red"),
                        tickfont=dict(color="red"),
                        overlaying="y",
                        side="right"))
    elif len(valid_columns) == 3:
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x = df["Datetime"],
            y = df[valid_columns[0]],
            mode = "lines",
            name = valid_columns[0],
            line = dict(color="blue")
            ))
        
        fig.add_trace(go.Scatter(
            x = df["Datetime"],
            y = df[valid_columns[1]],
            mode = "lines",
            name = valid_columns[1],
            line = dict(color="red"),
            yaxis="y2"
            ))
        
        fig.add_trace(go.Scatter(
            x = df["Datetime"],
            y = df[valid_columns[2]],
            mode = "lines",
            name = valid_columns[2],
            line = dict(color="green"),
            yaxis="y3"
            ))
        
        fig.update_layout(
            title=f"{signali[valid_columns[0]]['longtxt']}",
            template="plotly",
            legend=dict(title="Legenda",
                        indentation=10),
            xaxis=dict(showgrid=True),
            yaxis=dict(showgrid=True,
                       zeroline=True,
                       title=signali[valid_columns[0]]["label"] + " [" + signali[valid_columns[0]]["unit"] + "]",
                       titlefont=dict(color="blue"),
                       tickfont=dict(color="blue")),
            yaxis2=dict(showgrid=True,
                        zeroline=True,
                        title=signali[valid_columns[1]]["label"] + " [" + signali[valid_columns[1]]["unit"] + "]",
                        titlefont=dict(color="red"),
                        tickfont=dict(color="red"),
                        overlaying="y",
                        side="right"),
            yaxis3=dict(showgrid=True,
                        zeroline=True,
                        title=signali[valid_columns[2]]["label"] + " [" + signali[valid_columns[2]]["unit"] + "]",
                        titlefont=dict(color="green"),
                        tickfont=dict(color="green"),
                        overlaying="y",
                        side="right"))
    
    for i in range(0, len(annotations), 2):
        if df["Datetime"].min() <= annotations[i+1] <= df["Datetime"].max(): 
            fig.add_vline(
                x=pd.to_datetime(annotations[i+1]).to_pydatetime(),
                line_width=1,
                line_dash="dash",
                line_color="#754FC5"
                )
            if i==2 :
                ay_set = -60
            else:
                ay_set = -40
                
            if i == 6:
                ax_set = 80
            else:
                ax_set = 20
                
            fig.add_annotation(
                x=pd.to_datetime(annotations[i+1]).to_pydatetime(),
                y=0.9,  # Set a relevant y-axis value
                xref="x",
                yref="paper",
                text=annotations[i],
                showarrow=True,
                arrowhead=2,
                ax=ax_set,  # Arrow shift in x direction
                ay=ay_set,  # Arrow shift in y direction
                font=dict(color="#754FC5", size=12),
                bordercolor="#754FC5",
                borderwidth=1,
                bgcolor="rgba(255,255,255,0.7)"
                )    
    return fig

# =============================================================================
#                               FOLDERS
# =============================================================================

savepath = r"""C:\Users\larab\Documents\GitHub\admilara.github.io\turbinska"""
datapath_cs = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\GEPPERT\cs"""

signali = {
    '00_speed_setpoint': {
        'unit': '%',
        'label': 'n',
        'longtxt': 'Brzina vrtnje',
        },
    '01_opening_sp': {
        'unit': '%',
        'label': 'y',
        'longtxt': 'Otvor privodnog kola',
        },
    '02_gate_servo_feedback': {
        'unit': '%',
        'label': 'y',
        'longtxt': 'Otvor privodnog kola'
        },
    '03_power_sp': {
        'unit': 'MW',
        'label': 'Pset',
        'longtxt': 'Radna snaga generatora',
        },
    '04_actual_opening': {
        'unit': '%',
        'label': 'y',
        'longtxt': 'Otvor privodnog kola'},
    '05_actual_power': {
        'unit': 'MW',
        'label': 'Pg',
        'longtxt': 'Radna snaga generatora',
        },
    '06_power_pid_out': {
        'unit': 'pu' ,
        'label': 'Signali regulatora',
        'longtxt': 'Signali regulatora',
        },
    '07power_pid_fwd_o': {
        'unit': 'pu',
        'label': 'Signali regulatora',
        'longtxt': 'Signali regulatora',
        },
    '08_speed_pidout': {
        'unit': 'pu',
        'label': 'Signali regulatora',
        'longtxt': 'Signali regulatora',
        },
    '10_grid_freq': {
        'unit': 'pu',
        'label': 'f',
        'longtxt': 'Mrežna frekvencija',
        },
    '11_blackstart_on':{ # pravi signal detekcije OR - 12_islandmod_det je nešto drugo, ne znam šta
        'unit': 'pu',
        'label': 'Crni start',
        'longtxt': 'Nalog početka crnog starta'
        },
    '13_actualspeed': {
        'unit': '%',
        'label': 'n',
        'longtxt': 'Brzina vrtnje',
        },
    '15_remote_speed_sp': {
        'unit': '%',
        'label': 'n',
        'longtxt': 'Brzina vrtnje',
        },
    }

gens = ["AGR-A", "AGR-B", "AGR-C", "AGR-D"]

timestamps = {"AGR-A": [],
              "AGR-B": [],
              "AGR-C": [],
              "AGR-D": []}

# =============================================================================
#                   ANOTACIJE ZA GRAFOVE
# =============================================================================

line_volt_txt = "Stavljanje DV 110 kV Zakučac - Meterize 3 pod napon"
line_volt_dt_str = "2024-12-03 11:46:54"
line_volt_dt = datetime.strptime(line_volt_dt_str, '%Y-%m-%d %H:%M:%S')
        
switch_txt = "Uklop sabirničkog rastavljača u polju blok trafoa D"
switch_dt_str = "2024-12-03 11:44:35"
switch_dt = datetime.strptime(switch_dt_str, '%Y-%m-%d %H:%M:%S')
        
off_txt = "Nalog za isključenje DV Zakučac - Meterize 3"
off_dt_str = "2024-12-03 12:18:59"
off_dt = datetime.strptime(off_dt_str, '%Y-%m-%d %H:%M:%S')
annotations = [line_volt_txt, line_volt_dt, switch_txt, switch_dt, 
                       off_txt, off_dt]
timestamps["AGR-D"] = annotations

# ---------------------------------------------------------------------------

line_volt_txt = "Stavljanje DV 220 kV Zakučac - Konjsko pod napon"
line_volt_dt_str = "2024-12-03 14:09:30"
line_volt_dt = datetime.strptime(line_volt_dt_str, '%Y-%m-%d %H:%M:%S')

switch_txt = "Uklop sabirničkog rastavljača u polju blok trafoa B"
switch_dt_str = "2024-12-03 14:07:30"
switch_dt = datetime.strptime(switch_dt_str, '%Y-%m-%d %H:%M:%S')

off_txt = "Nalog za isključenje DV Zakučac - Konjsko"
off_dt_str = "2024-12-03 14:55:29"
off_dt = datetime.strptime(off_dt_str, '%Y-%m-%d %H:%M:%S')  

at3_txt = "Energizacija AT3"
at3_dt_str = "2024-12-03 14:20:25.394"
at3_dt = datetime.strptime(at3_dt_str, '%Y-%m-%d %H:%M:%S.%f')

annotations = [line_volt_txt, line_volt_dt, switch_txt, switch_dt, 
               off_txt, off_dt, at3_txt, at3_dt]

timestamps["AGR-B"] = annotations

# ---------------------------------------------------------------------------

line_volt_txt = "Stavljanje DV 110 kV Zakučac - Meterize 3 pod napon"
line_volt_dt_str = "2024-12-03 09:43:06"
line_volt_dt = datetime.strptime(line_volt_dt_str, "%Y-%m-%d %H:%M:%S")

switch_txt = "Uklop sabirničkog rastavljača u polju blok trafoa A"
switch_dt_str = "2024-12-03 09:38:32"
switch_dt = datetime.strptime(switch_dt_str, "%Y-%m-%d %H:%M:%S")

off_txt = "Nalog za isključenje DV Zakučac - Meterize 3"
off_dt_str = "2024-12-03 10:32:02"
off_dt = datetime.strptime(off_dt_str, "%Y-%m-%d %H:%M:%S")

annotations = [line_volt_txt, line_volt_dt, switch_txt, switch_dt, off_txt, off_dt]

timestamps["AGR-A"] = annotations

# ---------------------------------------------------------------------------

line_volt_txt = "Stavljanje DV 220 kV Zakučac - Konjsko pod napon"
line_volt_dt_str = "2024-12-03 15:54:29"
line_volt_dt = datetime.strptime(line_volt_dt_str, "%Y-%m-%d %H:%M:%S")

switch_txt = "Uklop sabirničkoj rastavljača u polju blok trafoa C"
switch_dt_str = "2024-12-03 15:49:49"
switch_dt = datetime.strptime(switch_dt_str, "%Y-%m-%d %H:%M:%S")

off_txt = "Nalog za isključenje DV 220 kV Zakučac - Konjsko"
off_dt_str = "2024-12-03 16:17:52"
off_dt = datetime.strptime(off_dt_str, "%Y-%m-%d %H:%M:%S")

annotations = [line_volt_txt, line_volt_dt, switch_txt, switch_dt, off_txt, off_dt]
timestamps["AGR-C"] = annotations

# ---------------------------------------------------------------------------

all_asc_files = {}
files_cs = [f for f in listdir(datapath_cs) if f.endswith('.ASC')]
    
for file in files_cs:
    path = datapath_cs + '\\' + file
    all_asc_files[file] = {}
    all_asc_files[file]["path"] = path
    
# print(all_asc_files)

# File path

for key, value in all_asc_files.items(): 
    file_path = value["path"]
    
    file_name = key
    # Regex pattern to include both header and data rows
    pattern = re.compile(r"^(Date;Time;.+|^\d{1,2}\.\d{1,2}\.\d{4};\d{2}:\d{2}:\d{2},\d;.+)$")

    # Read the file and filter lines
    with open(file_path, "r", encoding="utf-8") as file:
        filtered_lines = [line.strip() for line in file if pattern.match(line)]

    # Convert the filtered lines to a single string for pandas
    data_string = "\n".join(filtered_lines)

    # Load the data into a DataFrame using pandas
    df = pd.read_csv(StringIO(data_string), sep=";")

    # Display the DataFrame
    #print(df.columns)
    df = df.rename(columns={"Gate_Servo_Feedb []": "02_Gate_Servo_Feedb []"})
    df = df.drop(columns={"12: IslandMode_DET []"})
    #print(df.columns)
    # Chain za preimenovanje stupaca - nekonzistentno imenovanje
    # sve u lowercase, izbačene nepotrebne [] zagrade, svi spaceovi prebačeni u _, ali izbačen zadnji space tj. _
    df.columns = (
        df.columns
        .str.strip()                           
        .str.replace(r'[^\w\s]', '', regex=True)
        .str.replace(r'\s+', '_', regex=True)
        .str.lower()
        .str.rstrip('_')
    )
    
    df = df.dropna(axis=1, how='all')
    for column in df.columns:
        if column == "date" or column == "time" or column == "Datetime":
            continue
        else:
            df[column] = df[column].str.replace(',', '.', regex=False)
            df[column] = pd.to_numeric(df[column], errors='coerce')
    df['Datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'], format='%d.%m.%Y %H:%M:%S,%f')
    
    all_asc_files[key]["df"] = df
    #print(df.columns)
    
    
column_list = signali.keys()

for key, fileset in all_asc_files.items():
    df = fileset["df"]
    filename = key.split('.')[0]
    filename = filename.replace("_", "-")
    
    gen_name = next((gen for gen in gens if gen in filename), None)
    
    grouped_signals = {}
    figs = []
    htmls = []
    for signal, meta in signali.items():
        longtxt = meta['longtxt']
        if longtxt not in grouped_signals:
            grouped_signals[longtxt] = []
        grouped_signals[longtxt].append(signal)
    print(grouped_signals)
    
    for key, value in grouped_signals.items():        
        fig = draw(df, key, value, timestamps[gen_name])
        figs.append(fig)

    
    for index, fig in enumerate(figs):
        if index == 0:
            html = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
        else:
            html = pio.to_html(fig, full_html=False, include_plotlyjs=False)
        htmls.append(html)
    divs_html = "\n".join(f"<div>{html}</div>" for html in htmls)

    html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{filename}</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </head>
        <body>
            <h3>{gen_name} - {filename}</h3>
            {divs_html}
            </body>
        </html>
        """
    with open(f"{savepath}\\{filename.lower()}.html", "w") as file:
        file.write(html_content)

