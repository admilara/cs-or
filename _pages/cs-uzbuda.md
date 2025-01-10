---
layout: default
title: CRNI START - REZULTATI INEM - UZBUDA
description: Kratki pregled podataka Končar INEM-a za pokuse crnog starta u HE Zakučac
---

<h1 style="text-align: center; font-family: Helvetica; color: red">03.12.2024. Crni start</h1>
<h2 style="text-align: center; font-family: Helvetica; color: red">Podatci: Končar INEM</h2>

Za pokuse crnog starta agregata A, D, B i C u HE Zakučac dostupni su i zapisi iz sustava uzbude,
dostavljeni u obliku RecEx i Watch log datoteka. Trajanje svih RecEx datoteka iznosi **2 minute, 13 sekundi i 56 milisekundi**.
Watch logovi različite su duljine te su one navedene u tablici ispod. 

Veličine u zapisima se razlikuju od datoteke do datoteke - popis oznaka, mjernih jedinica i baznih vrijednosti veličina koje se mogu naći u datotekama nalazi se ispod tablice. 

primjer linka <td style="text-align:center"><a href="{{ site.baseurl }}/cs-agregata-d-pmu-323/">PMU#318</a></td>
recex_zakuca1a_003.log
{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica; color: red">Zapis</th>
            <th style="text-align:center; font-family: Helvetica; color: red">Agregat A</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa</th>
            <th style="text-align:center; font-family: Helvetica; color: red">Agregat D</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa</th>
            <th style="text-align:center; font-family: Helvetica; color: red">Agregat B</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa</th>
            <th style="text-align:center; font-family: Helvetica; color: red">Agregat C</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa</th>            
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">RECEX LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/recex_zakuca1a_003.log/">RecEx_ZAKUCA1A_003.log</a></td>
            <td style="text-align:center">0:02:13.056000</td>
            <td style="text-align:center">RecEx_ZAKUCA1D_001.log</td>
            <td style="text-align:center">0:02:13.056000</td>
            <td style="text-align:center">RecEx_ZAKUCA1B_001.log</td>
            <td style="text-align:center">0:02:13.056000</td>
            <td style="text-align:center">RecEx_ZAKUCA1C_034.log</td>
            <td style="text-align:center">0:02:13.056000</td>
        </tr>
        <tr>
            <td style="text-align:center">WATCH LOG</td>
            <td style="text-align:center">Watch_ZAKUCA1A_006.log</td>
            <td style="text-align:center">00:02:45.652000</td>
            <td style="text-align:center">Watch_ZAKUCA1D_006.log</td>
            <td style="text-align:center">00:03:50.937000</td>            
            <td style="text-align:center">Watch_ZAKUCA1B_001.log</td>
            <td style="text-align:center">00:04:25.700000</td>
            <td style="text-align:center">Watch_ZAKUCA1C_007.log</td>
            <td style="text-align:center">00:03:29.419000</td>
        </tr>
        <tr>
            <td style="text-align:center"></td>
            <td style="text-align:center">Watch_ZAKUCA1A_007.log</td>
            <td style="text-align:center">00:03:54.593000</td>
            <td style="text-align:center">Watch_ZAKUCA1D_007.log</td>
            <td style="text-align:center">00:03:31.879000</td>
            <td style="text-align:center">Watch_ZAKUCA1B_012.log</td>
            <td style="text-align:center">00:03:47.137000</td>
            <td style="text-align:center">Watch_ZAKUCA1C_008.log</td>
            <td style="text-align:center">00:03:31.128000</td>
        </tr>
        <tr>
            <td style="text-align:center"></td>
            <td style="text-align:center">Watch_ZAKUCA1A_008.log</td>
            <td style="text-align:center">00:03:03.001000</td>
            <td style="text-align:center">-</td>
            <td style="text-align:center">-</td>
            <td style="text-align:center">Watch_ZAKUCA1B_013.log</td>
            <td style="text-align:center">00:07:07.524000</td>
            <td style="text-align:center">-</td>
            <td style="text-align:center">-</td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}





