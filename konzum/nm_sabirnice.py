# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 11:59:26 2025

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
    
    
# =============================================================================
#                       PREP CSV (katastrofa :( )
# =============================================================================

file = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\HOPS\mjerenja\sabirnice\TS_KONJ_SAB_20241204_0910-1710.csv"""

df = pd.read_csv(file, header=0, delimiter = ";;", engine="python")
#print(df.columns)

#print(df.iloc[0])
columns = list(df.columns)
for i, column in enumerate(columns):
    if "Unnamed" in column:
        name_before = columns[i-1]
        columns[i] = name_before
        columns[i-1] = f"timestamp {name_before}"
        
df.columns = columns
print(df.columns)

str_to_remove = ["KONJ", "SKO", "MP", "W12", "DAS", "SAB"]

df.columns = df.columns.to_series()

for string in str_to_remove:
    df.columns = df.columns.str.replace(string, "", regex=False)

df.columns = df.columns.str.replace(" +", " ", regex=True).str.strip()
print(df.columns)


# 3. Lowercase and snake_case
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 4. Optional: custom replacements
column_renames = {
    "das_frekvencija_w1": "freq W1",
    "das_frekvencija_w2": "freq W2",
    "frekvencija_w1": "freq W1",
    "frekvencija_w2": "freq W2",
    "napon_w1": "voltage W1",
    "napon_w2": "voltage W2",
    "u_w1a": "voltage W1",
    "u_w2a": "voltage W2",
}

# Also apply these replacements to timestamp-prefixed names
timestamp_renames = {f"timestamp_{k}": f"timestamp_{v}" for k, v in column_renames.items()}

# Merge both mappings
column_renames.update(timestamp_renames)

# 5. Rename columns based on mapping
df = df.rename(columns=column_renames)
print(df.columns)

df = df.dropna(axis = 1, how = 'all')


named_dfs = {}
columns = df.columns

for i in range(0, len(columns), 2):
    base_name = columns[i+1]
    named_dfs[base_name] = df[[columns[i], columns[i+1]]].copy()

    
# =============================================================================
#               GRAFOVI    
# =============================================================================

otocni_rad = [("2024-12-04 09:12:58", "HE ZAK 110 METERIZE/2", "2024-12-04 10:20:29", "HE ZAK 110 SP W12", "TS KONJSKO"),
              ("2024-12-04 11:48:26", "HE ZAK 110 METERIZE/2", "2024-12-04 12:47:14", "HE ZAK 110 SP W12", "TS KONJSKO"),
              ("2024-12-04 14:24:28", "HE ZAK 110 METERIZE/2", "2024-12-04 15:25:27", "HE ZAK 110 SP W12", "TS KONJSKO"),
              ("2024-12-04 16:27:27", "HE ZAK 110 METERIZE/2", "2024-12-04 17:03:18", "HE ZAK 220 SP W12", "TS KONJSKO")]


signals = ["110_napon_w1", "110_napon_w2", "220_napon_w1", "220_napon_w2"]
gens = ["A", "D", "B", "C"]

volt_path = r"""C:\Users\larab\Documents\GitHub\cs-or\cs-or\konzum\voltage-regulation.xlsx"""
df_annotations = pd.read_excel(volt_path)
df_annotations['timestamp'] = pd.to_datetime(df_annotations['timestamp'], dayfirst=True)




for i, (start_time, start_label, end_time, end_label, station) in enumerate(otocni_rad, start=1):
    start = pd.to_datetime(start_time)
    end = pd.to_datetime(end_time)
    
    fig = make_subplots(rows=2, cols=2, subplot_titles=[s.replace("_", " ").upper() for s in signals])
    
    
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

        yaxis_title = "U [kV]" if "napon" in df_value else "f [Hz]"
        single_fig = plot(df_subset, df_time, df_value, yaxis_title=yaxis_title)

        row = idx // 2 + 1
        col = idx % 2 + 1
        #row = idx+1
        #col = 1
        for trace in single_fig.data:
            fig.add_trace(trace, row=row, col=col)

        fig.update_xaxes(title_text="Vrijeme", row=row, col=col)
        fig.update_yaxes(title_text=yaxis_title, row=row, col=col)
        
        
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
                    xref="x",
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
        title_text=f"Otočni rad {gens[i-1]}: {start_time} → {end_time}, mjerenja u {station}",
        showlegend=False,
        template="plotly_white"
    )

    filename = f"otocni-rad-{gens[i-1].lower()}-naponi-konjsko.html"
    plotly.offline.plot(fig, filename=filename)
    print(f"Saved {filename}")



