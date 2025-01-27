# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:38:41 2024

@author: Lara Buljan
"""

import plotly
import plotly.graph_objects as go
import plotly.io as pio
from plotly.offline import plot
#import plotly.dashboard_objs as dashboard_objs
import IPython.display
#from IPyhton.display import Image

from datetime import datetime

from os import listdir
from os.path import isfile, join

import pandas as pd


def graf_radna_jalova(df, unit):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_RADNA_SNAGA_GENERATORA"],
        mode="lines",
        name=f"RADNA SNAGA GENERATORA {unit} [MW]",
        line=dict(color="red")
        ))

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_JALOVA_SNAGA_GENERATORA"],
        mode="lines",
        name=f"JALOVA SNAGA GENERATORA {unit} [Mvar]",
        line=dict(color="blue"),
        yaxis="y2"
        ))

    fig.update_layout(
        title=f"Radna i jalova snaga generatora {unit}",
        xaxis_title="Vrijeme",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True,
                   title="Pg [MW]",
                   titlefont=dict(color="red"),
                   tickfont=dict(color="red")),
        yaxis2=dict(showgrid=True,
                    title="Qg [Mvar]",
                    titlefont=dict(color="blue"),
                    tickfont=dict(color="blue"),
                    overlaying="y",
                    side="right")
        )
    return fig


def graf_naponi_gen(df, unit):
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_NAPON_GENERATORA_UL1L2"],
        mode="lines",
        name=f"NAPON GENERATORA {unit} - UL1L2 [V]",
        line=dict(color="blue")))

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_NAPON_GENERATORA_UL2L3"],
        mode="lines",
        name=f"NAPON GENERATORA {unit} - UL2L3 [V]",
        line=dict(color="red")))

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_NAPON_GENERATORA_UL3L1"],
        mode="lines",
        name=f"NAPON GENERATORA {unit} - UL3L1 [V]",
        line=dict(color="green")))

    fig.update_layout(
        title=f"Naponi generatora {unit}",
        xaxis_title="Timestamp",
        yaxis_title="Ug [V]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
        )
    return fig


def graf_struje_gen(df, unit):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_STRUJA_GENERATORA_IL1"],
        mode="lines",
        name=f"STRUJA GENERATORA {unit} - IL1 [A]",
        line=dict(color="blue")))

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_STRUJA_GENERATORA_IL2"],
        mode="lines",
        name=f"STRUJA GENERATORA {unit} - IL2 [A]",
        line=dict(color="red")))

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_STRUJA_GENERATORA_IL3"],
        mode="lines",
        name=f"STRUJA GENERATORA {unit} - IL3 [A]",
        line=dict(color="green")))

    fig.update_layout(
        title=f"Struje generatora {unit}",
        xaxis_title="Vrijeme",
        yaxis_title="Ig [V]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
        )
    
    return fig


def graf_uzbuda(df, unit):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_NAPON_UZBUDE"],
        mode="lines",
        name=f"NAPON UZBUDE GENERATORA {unit} [V]",
        line=dict(color="blue")))

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_STRUJA_UZBUDE"],
        mode="lines",
        name=f"STRUJA UZBUDE GENERATORA {unit} [A]",
        line=dict(color="red"),
        yaxis="y2"))

    fig.update_layout(
        title=f"Napon i struja uzbude generatora {unit}",
        xaxis_title="Vrijeme",
        yaxis_title="Napon i struja uzbude",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True,
                   title="Uf [V]",
                   titlefont=dict(color="blue"),
                   tickfont=dict(color="blue")),
        yaxis2=dict(showgrid=True,
                    title="If [A]",
                    titlefont=dict(color="red"),
                    tickfont=dict(color="red"),
                    overlaying="y",
                    side="right")
        )
    return fig


def graf_brzine(df, unit):
    fig = go.Figure()
        
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_FREKVENCIJA_GENERATORA"]/50*100,
        mode="lines",
        name=f"FREKVENCIJA GENERATORA {unit} [%]",
        line=dict(color="blue")
        ))
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"PB_{unit}_TR_ZADANA_BRZ"],
        mode="lines",
        name=f"ZADANA BRZINA VRNJE GENERATORA {unit} [%]",
        line=dict(color="black")
        ))
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"PB_{unit}_TR_BRZINA_VRTNJE"],
        mode="lines",
        name=f"BRZINA VRTINJE GENERATORA {unit} [%]",
        line=dict(color="green")
        ))
    
    fig.update_layout(
        title=f"Frekvencija, brzina vrtnje i zadana brzina vrtnje jedinice {unit}",
        xaxis_title="Vrijeme",
        yaxis_title="f, n, nset [%]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
        )
    
    return fig

def graf_frekvencija(df, unit):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_FREKVENCIJA_GENERATORA"],
        mode="lines",
        name=f"FREKVENCIJA GENERATORA {unit} [Hz]",
        line=dict(color="purple")
        ))
    
    fig.update_layout(
        title=f"Frekvencija jedinice {unit}",
        xaxis_title="Vrijeme",
        yaxis_title="f [Hz]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)        
        )
    return fig

def graf_otvor_pk(df, unit):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"PB_{unit}_TR_OTVOR_PK"],
        mode="lines",
        name=f"OTVOR PRIVODNOG KOLA {unit} [%]",
        line=dict(color="blue")
        ))
    
    fig.update_layout(
        title=f"Otvor privodnog kola jedinice {unit}",
        xaxis_title="Vrijeme",
        yaxis_title="y [%]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
        )
    return fig

def graf_otvor_pk(df, unit):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"PB_{unit}_TR_OTVOR_PK"],
        mode="lines",
        name=f"OTVOR PRIVODNOG KOLA {unit} [%]",
        line=dict(color="blue")
        ))
    
    fig.update_layout(
        title=f"Otvor privodnog kola jedinice {unit}",
        xaxis_title="Vrijeme",
        yaxis_title="y [%]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
        )
    return fig

def graf_tlak(df, unit):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_TLAK_U_SPIRALI_TURBINE"],
        mode="lines",
        name=f"TLAK U SPIRALI TURBINE JEDINICE {unit} [bar]",
        line=dict(color="blue")
        ))
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_TLAK_U_TLACNOM_CJEVOVODU"],
        mode="lines",
        name=f"TLAK U TLACNOM CJEVOVODU [bar]",
        line=dict(color="red")
        ))
    
    fig.update_layout(
        title=f"Tlakovi za vrijeme CS jedinice {unit}",
        xaxis_title="Vrijeme",
        yaxis_title="p [bar]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)        
        )
    return fig


def graf(gen, df, signal_dict, annotations):
    print(f"U funkciji: {gen}")
    fig = go.Figure()
    
    if isinstance(signal_dict["yaxis"], list):
        print(f"U if dijelu: {gen}")
        fig.add_trace(go.Scatter(
            x=df["Vrijeme"],
            y=df[signal_dict["signals"][0].format(unit=gen)],
            mode="lines",
            name=signal_dict["name"][0].format(unit=gen),
            line=dict(color=signal_dict["colors"][0])
            ))
        fig.add_trace(go.Scatter(
            x=df["Vrijeme"],
            y=df[signal_dict["signals"][1].format(unit=gen)],
            mode="lines",
            name=signal_dict["name"][1].format(unit=gen),
            line=dict(color=signal_dict["colors"][1]),
            yaxis="y2"
            ))
        fig.update_layout(
            title=signal_dict["title"].format(unit=gen),
            xaxis_title="Vrijeme",
            template="plotly",
            legend_title="Legenda",
            xaxis=dict(showgrid=True),
            yaxis=dict(showgrid=True,
                       title=signal_dict["yaxis"][0],
                       titlefont=dict(color=signal_dict["colors"][0]),
                       tickfont=dict(color=signal_dict["colors"][0])),
            yaxis2=dict(showgrid=True,
                        title=signal_dict["yaxis"][1],
                        titlefont=dict(color=signal_dict["colors"][1]),
                        tickfont=dict(color=signal_dict["colors"][1]),
                        overlaying="y",
                        side="right")
            )
    else:
        print(f"U else dijelu: {gen}")
        for index, signal in enumerate(signal_dict["signals"]):
            fig.add_trace(go.Scatter(
                x=df["Vrijeme"],
                y=df[signal.format(unit=gen)],
                mode="lines",
                name=signal_dict["name"][index].format(unit=gen),
                line=dict(color=signal_dict["colors"][index])
                ))
        fig.update_layout(
            title=signal_dict["title"].format(unit=gen),
            xaxis_title="Vrijeme",
            yaxis_title=signal_dict["yaxis"],
            template="plotly",
            legend_title="Legenda",
            xaxis=dict(showgrid=True),
            yaxis=dict(showgrid=True)        
            )
    
    for i in range(0, len(annotations), 2):
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
#                   START - LOKACIJA FILEOVA
# =============================================================================

mypath = "D:\\3_RADNO\\_HOPS\\2_ZAKUCAC_CS_OP\\KET"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

savepath = r"""C:\Users\larab\Documents\GitHub\admilara.github.io\konzum\htmls"""

for file in files:
    print(file)
    print("\n")

gens=["A", "B", "C", "D"]
units = {"A": {},
         "B": {},
         "C": {},
         "D": {}}


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
units["D"]["annotations"] = annotations

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

units["B"]["annotations"] = annotations

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

units["A"]["annotations"] = annotations

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
units["C"]["annotations"] = annotations

# =============================================================================
#                           SVI SIGNALI
# =============================================================================

mjerenja = {"Naponi": {"signals": ["{unit}_NAPON_GENERATORA_UL1L2",
                                   "{unit}_NAPON_GENERATORA_UL2L3",
                                   "{unit}_NAPON_GENERATORA_UL3L1"],
                       "colors": ["red", "blue", "green"],
                       "name": ["NAPON GENERATORA {unit} - UL1L2 [V]",
                                "NAPON GENERATORA {unit} - UL2L3 [V]",
                                "NAPON GENERATORA {unit} - UL3L1 [V]"],
                       "yaxis": "Ug [V]",
                       "title": "Naponi generatora {unit}"
                       },
            "Struje": {"signals": ["{unit}_STRUJA_GENERATORA_IL1",
                                   "{unit}_STRUJA_GENERATORA_IL2",
                                   "{unit}_STRUJA_GENERATORA_IL3"],
                       "colors": ["red", "blue", "green"],
                       "name": ["STRUJA GENERATORA {unit} - IL1 [A]",
                                "STRUJA GENERATORA {unit} - IL2 [A]",
                                "STRUJA GENERATORA {unit} - IL3 [A]"],
                       "yaxis": "Ig [A]",
                       "title": "Struje generatora {unit}"},
            "Uzbuda": {"signals": ["{unit}_NAPON_UZBUDE",
                                   "{unit}_STRUJA_UZBUDE"],
                       "colors": ["red", "blue"],
                       "name": ["NAPON UZBUDE GENERATORA {unit} [V]",
                                "STRUJA UZBUDE GENERATORA {unit} [A]"],
                       "yaxis": ["Uf [V]", "If [V]"],
                       "title": "Napon i struja uzbude generatora {unit}"},
            "Brzina": {"signals": ["PB_{unit}_TR_ZADANA_BRZ",
                                   "PB_{unit}_TR_BRZINA_VRTNJE"],
                       "colors": ["red", "blue"],
                       "name": ["ZADANA BRZINA VRTNJE GENERATORA {unit} [%]",
                                "BRZINA VRTNJE GENERATORA {unit} [%]"],
                       "yaxis": "n, nset [%]",
                       "title": "Brzina vrtnje i zadana brzina vrtnje jedinice {unit}"},
            "Frekvencija": {"signals": ["{unit}_FREKVENCIJA_GENERATORA"],
                            "colors": ["red"],
                            "name": ["FREKVENCIJA GENERATORA {unit} [Hz]"],
                            "yaxis": "f [Hz]",
                            "title": "Frekvencija jedinice {unit}"},
            "Otvor_PK": {"signals": ["PB_{unit}_TR_OTVOR_PK"],
                         "colors": ["blue"],
                         "name": ["OTVOR PRIVODNOG KOLA {unit} [%]"],
                         "yaxis": "y [%]",
                         "title": "OTVOR PRIVODNOG KOLA JEDINICE {unit}"},
            "Tlak": {"signals": ["{unit}_TLAK_U_SPIRALI_TURBINE",
                                 "{unit}_TLAK_U_TLACNOM_CJEVOVODU"],
                     "colors": ["red", "blue"],
                     "name": ["TLAK U SPIRALI TURBINE JEDINICE {unit} [bar]",
                              "TLAK U TLACNOM CJEVOVODU [bar]"],
                     "yaxis": "p [bar]",
                     "title": "Tlakovi za vrijeme CS jedinice {unit}"},
            "Snaga": {"signals": ["{unit}_RADNA_SNAGA_GENERATORA",
                                  "{unit}_JALOVA_SNAGA_GENERATORA"],
                      "colors": ["red", "blue"],
                      "name": ["RADNA SNAGA GENERATORA {unit} [MW]",
                               "JALOVA SNAGA GENERATORA {unit} [Mvar]"],
                      "yaxis": ["P [MW]", "Q [Mvar]"],
                      "title": "Radna i jalova snaga generatora {unit}"}
            }



cs_files = [file for file in files if "crni start" in file]
cs = [file for file in cs_files if "Agregat" in file]
print(cs)

#cs_df = pd.read_excel(mypath + "\\" + cs[2], header=1)

for i in range(4):
    if "Agregat A" in cs[i]:
        crni_start_df = pd.read_excel(mypath + "\\" + cs[i], header=0)
        crni_start_df = crni_start_df.drop(0)
    else:
        crni_start_df = pd.read_excel(mypath + "\\" + cs[i], header=1)

    crni_start_df["Vrijeme"] = pd.to_datetime(crni_start_df["Vrijeme"], format="%d-%m-%Y %H:%M:%S", dayfirst=True)
    units[gens[i]]["df"] = crni_start_df
    print(f"Done - {cs[i]}")

    
for unit, value in units.items():
    fig_list = []
    for mjerenje_naziv, mjerenje_podatci in mjerenja.items():
        fig0 = graf(unit, value["df"], mjerenja[mjerenje_naziv], value["annotations"]) 
        fig_list.append(fig0)
    
    html_list=[]
    for fig in fig_list:
        if not html_list:
            html = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
            html_list.append(html)
        else:
            html = pio.to_html(fig, full_html=False, include_plotlyjs=False)
            html_list.append(html)
    
    divs_html = "\n".join(f"<div>{html}</div>" for html in html_list)
        
    html_page = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>gen-{unit}-CS</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    </head>
    <body>
        <h2>Vizualizacija podataka - PROCIS</h2>
        {divs_html}
    </body>
    </html>
    """
    
    # Save the HTML page
    with open(f"procis-cs-gen-{unit.lower()}.html", "w") as f:
        f.write(html_page)
    
    print(f"Dashboard saved as PROCIS-CS-GEN-{unit.lower()}.html")