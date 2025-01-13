---
layout: default
title: OTOČNI RAD - REZULTATI INEM - UZBUDA
description: Kratki pregled podataka Končar INEM-a za pokuse otočnog rada u HE Zakučac
---

<h1 style="text-align: center; font-family: Helvetica; color: red">04.12.2024. Otočni rad</h1>
<h2 style="text-align: center; font-family: Helvetica; color: red">Podatci: Končar INEM</h2>

Za pokuse otočnog rada agregata A, D, B i C u HE Zakučac dostupni su i zapisi iz sustava uzbude,
dostavljeni u obliku RecEx i Watch log datoteka. Trajanje RecEx datoteka iznosi **2 minute, 13 sekundi i 56 milisekundi**.
Watch logovi različite su duljine te su one navedene u tablici ispod. 

Veličine u zapisima se razlikuju od datoteke do datoteke - popis oznaka, mjernih jedinica i baznih vrijednosti veličina koje se mogu naći u datotekama nalazi se ispod tablice. 

{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica; color: red">Zapis</th>
            <th style="text-align:center; font-family: Helvetica; color: red">Agregat A</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa</th>
            <th style="text-align:center; font-family: Helvetica; color: red">Agregat D</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa</th>>            
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">RECEX LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/recex_zakuca1a_006/">RecEx_ZAKUCA1A_006.log</a></td>
            <td style="text-align:center">0:02:13.056000</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/recex_zakuca1d_003/">RecEx_ZAKUCA1D_003.log</a></td>
            <td style="text-align:center">0:02:13.056000</td>
        </tr>
        <tr>
            <td style="text-align:center">WATCH LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch_zakuca1a_031/">Watch_ZAKUCA1A_031.log</a></td>
            <td style="text-align:center">00:01:49.757000</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch_zakuca1d_022/">Watch_ZAKUCA1D_022.log</a></td>            
            <td style="text-align:center">00:04:30.850000</td>            
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}

{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica; color: red">Zapis</th>
            <th style="text-align:center; font-family: Helvetica; color: red">Agregat B</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa</th>
            <th style="text-align:center; font-family: Helvetica; color: red">Agregat C</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa</th>            
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">RECEX LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/recex_zakuca1b_002/">RecEx_ZAKUCA1B_002.log</a></td>
            <td style="text-align:center">0:02:13.056000</td>
            <td style="text-align:center">-</td>
            <td style="text-align:center">-</td>
        </tr>
        <tr>
            <td style="text-align:center">WATCH LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch_zakuca1b_031/">Watch_ZAKUCA1B_031.log</a></td>            
            <td style="text-align:center">00:03:49.270000</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch_zakuca1c_013/">Watch_ZAKUCA1C_013.log</a></td>            
            <td style="text-align:center">00:02:14.407000</td>
        </tr>
        <tr>
            <td style="text-align:center"></td>
            <td style="text-align:center">-</td>            
            <td style="text-align:center">-</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch_zakuca1c_022/">Watch_ZAKUCA1C_022.log</a></td>            
            <td style="text-align:center">00:00:46.87700</td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}






