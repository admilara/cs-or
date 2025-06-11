# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 14:00:07 2025

@author: larab
"""

import pandas as pd
import plotly.graph_objects as go
import plotly

from plotly.subplots import make_subplots

def prepare_df(df, time_col, value_col):
    df = df.copy()
    df[time_col] = pd.to_datetime(df[time_col], format="%d.%m.%Y. %H:%M:%S", dayfirst=True, errors='coerce')
    df[value_col] = df[value_col].astype(str).str.replace(",", '.').astype(float)
    return df


def plot(df, time_col, value_col, yaxis_title=None, color=None):
    fig=go.Figure()
    fig.add_trace(go.Scatter(
        x=df[time_col],
        y=df[value_col],
        mode="lines",
        line=dict(shape="hv"),
        name=value_col
        ))
    
    fig.update_layout(
        title=value_col,
        xaxis_title="Vrijeme",
        yaxis_title=yaxis_title or value_col,
        template="plotly_white",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        hovermode="x unified"
    )
    return fig

file1 = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\HOPS\mjerenja\mrežni TR\HE_ZAK_ATR1_20241204_0910-1710.csv"""
#file2 = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\HOPS\mjerenja\mrežni TR\TS_KONJ_ATR3_20241204_0910-1710.csv"""


df_zak_tr = pd.read_csv(file1, header=0, delimiter = ";;", engine="python")
#df_kon_tr = pd.read_csv(file2, header=0, delimiter= ";;", engine="python")
df_zak_tr = df_zak_tr.dropna(axis = 1, how = 'all')

columns = list(df_zak_tr.columns)
for i, column in enumerate(columns):
    if "Unnamed" in column:
        name_before = columns[i-1]
        columns[i] = name_before
        columns[i-1] = f"timestamp {name_before}"
        
df_zak_tr.columns = columns
print(df_zak_tr.columns)

# columns = list(df_kon_tr.columns)
# for i, column in enumerate(columns):
#     if "Unnamed" in column:
#         name_before = columns[i-1]
#         columns[i] = name_before
#         columns[i-1] = f"timestamp {name_before}"
        
# df_kon_tr.columns = columns
# print(df_kon_tr.columns)

dfs = [df_zak_tr]

str_to_remove = ["SM_NDC"]

for df in dfs:
    df.columns = df.columns.to_series()
    
    for string in str_to_remove:
        df.columns = df.columns.str.replace(string, "", regex=False)
    
    df.columns = df.columns.str.replace(" +", " ", regex=True).str.strip()
    print(df.columns)
    
    
    # 3. Lowercase and snake_case
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    
    # 4. Optional: custom replacements
    # column_renames = {
    #     "das_frekvencija_w1": "freq W1",
    #     "das_frekvencija_w2": "freq W2",
    #     "frekvencija_w1": "freq W1",
    #     "frekvencija_w2": "freq W2",
    #     "napon_w1": "voltage W1",
    #     "napon_w2": "voltage W2",
    #     "u_w1a": "voltage W1",
    #     "u_w2a": "voltage W2",
    # }
    
    # # Also apply these replacements to timestamp-prefixed names
    # timestamp_renames = {f"timestamp_{k}": f"timestamp_{v}" for k, v in column_renames.items()}
    
    # # Merge both mappings
    # column_renames.update(timestamp_renames)
    
    # # 5. Rename columns based on mapping
    # df = df.rename(columns=column_renames)
    # print(df.columns)
    
    df = df.dropna(axis = 1, how = 'all')
    
    named_dfs = {}
    columns = df.columns
    
    for i in range(0, len(columns), 2):
        base_name = columns[i+1]
        named_dfs[base_name] = df[[columns[i], columns[i+1]]].copy()
    
        
    # =============================================================================
    #               GRAFOVI    
    # =============================================================================
    
    otocni_rad = [("2024-12-04 09:12:58", "HE ZAK 110 METERIZE/2", "2024-12-04 10:20:29", "HE ZAK 110 SP W12", "ATR ZAKUCAC"),
                  ("2024-12-04 11:48:26", "HE ZAK 110 METERIZE/2", "2024-12-04 12:47:14", "HE ZAK 110 SP W12", "ATR ZAKUCAC"),
                  ("2024-12-04 14:24:28", "HE ZAK 110 METERIZE/2", "2024-12-04 15:25:27", "HE ZAK 110 SP W12", "ATR ZAKUCAC"),
                  ("2024-12-04 16:27:27", "HE ZAK 110 METERIZE/2", "2024-12-04 17:03:18", "HE ZAK 220 SP W12", "ATR ZAKUCAC")]
    
    signals = ["he_zak_220/110_atr_položaj_reg_sklopke"]
    gens = ["A", "D", "B", "C"]
    
    volt_path = r"""C:\Users\larab\Documents\GitHub\cs-or\cs-or\konzum\voltage-regulation.xlsx"""
    df_annotations = pd.read_excel(volt_path)
    df_annotations['timestamp'] = pd.to_datetime(df_annotations['timestamp'], dayfirst=True)
    
    titles = ["položaj reg sklopke atr - otočni rad agr A",
              "položaj reg sklopke atr - otočni rad agr D", 
              "položaj reg sklopke atr - otočni rad agr B",
              "položaj reg sklopke atr - otočni rad agr C"]
    rows = [1,1,2,2]
    cols = [1,2,1,2]
    
    fig = make_subplots(rows=2, cols=2, 
                        subplot_titles=[t.replace("_", " ").upper() for t in titles],
                        shared_xaxes=False, shared_yaxes=False)
    
    for i, (start_time, start_label, end_time, end_label, station) in enumerate(otocni_rad, start=1):
        start = pd.to_datetime(start_time)
        end = pd.to_datetime(end_time)
        
        for idx, signal in enumerate(signals):
            if signal not in named_dfs:
                print(f"Skipping {signal}: not found in named_dfs.")
                continue
    
            df = named_dfs[signal]
            df_time = df.columns[0]
            df_value = df.columns[1]
            df_clean = prepare_df(df, df_time, df_value)
    
            # Filter for otočni_rad window
            df_subset = df_clean[
                (df_clean[df_time] >= start) & (df_clean[df_time] <= end)
            ].copy()
    
            if df_subset.empty:
                print(f"Skipping {signal} for interval {i}: No data found.")
                continue
    
            # Use your plot() function to get the Figure
            #yaxis_title = "U [kV]" if "napon" in df_value else "f [Hz]"
            yaxis_title = "polozaj"
            single_fig = plot(df_subset, df_time, df_value, yaxis_title=yaxis_title)
    
        # Add trace from single_fig to the subplot
        row_fig = rows[i-1]
        col_fig = cols[i-1]
        #row = idx+1
        #col = 1
        for trace in single_fig.data:
            fig.add_trace(trace, row=row_fig, col=col_fig)

        # Optionally, update axes labels for each subplot
        fig.update_xaxes(title_text="Vrijeme", row=row_fig, col=col_fig,
                         range=[start, end])
        fig.update_yaxes(title_text=yaxis_title, row=row_fig, col=col_fig,
                         range=[0,11])
        
        
        if df_annotations is not None:        
            filtered_annotations = df_annotations[
                (df_annotations['timestamp'] >= start) & 
                (df_annotations['timestamp'] <= end)
            ]
        
            # Add annotations to the plot
            for j, (_, row) in enumerate(filtered_annotations.iterrows()):
                ts = pd.to_datetime(row['timestamp'])
                vertical_position = 0.95-(j*0.05)
                #if "(A)" in row["radnja"] or "(D)" in row["radnja"]:
                #    vertical_position = 1.05 + (i * 0.05)  # stack annotations
                #else:
                #    vertical_position = 0.95 - (i * 0.1)
                
                fig.add_vline(
                    x=ts,
                    line_width=1,
                    line_dash="dash",
                    )
                
                fig.add_annotation(
                    x=ts,
                    y=vertical_position,
                    xref=f"x{row_fig}",
                    yref="paper",
                    text=row['radnja'],
                    showarrow=True,
                    arrowhead=3,
                    ax=0,
                    ay=-40,
                    font=dict(size=10),
                    borderwidth=1,
                    bgcolor="rgba(255,255,255,0.9)"
                    )

    fig.update_layout(
        title_text=f"Ispitivanje sposobnosti OR HE Zakucac, mjerenja na {station}",
        showlegend=False,
        template="plotly_white"
    )

    # Save ONE html file per otočni_rad
    filename = "otocni-rad-polozaj-zakucac.html"
    plotly.offline.plot(fig, filename=filename)
    print(f"Saved {filename}")










