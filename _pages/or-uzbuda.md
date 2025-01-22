---
layout: default
title: OTOČNI RAD - REZULTATI INEM - UZBUDA
description: Kratki pregled podataka Končar INEM-a za pokuse otočnog rada u HE Zakučac
---

<style scoped>
table {
  font-size: 13px;
}
</style>

<h1 style="text-align: center; font-family: Helvetica; color: red">04.12.2024. Otočni rad</h1>
<h2 style="text-align: center; font-family: Helvetica; color: red">Podatci: Končar INEM</h2>

Za pokuse otočnog rada agregata A, D, B i C u HE Zakučac dostupni su i zapisi 
iz sustava uzbude, dostavljeni u obliku RecEx i Watch log datoteka. Trajanje 
RecEx datoteka iznosi **2 minute, 13 sekundi i 56 milisekundi**.
Watch logovi različite su duljine te su one navedene u tablici ispod. 

Veličine u zapisima se razlikuju od datoteke do datoteke - popis oznaka, 
mjernih jedinica i baznih vrijednosti veličina koje se mogu naći u datotekama 
nalazi se ispod linkova i u svakoj datoteci zasebno. 



{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica">Zapis</th>
            <th style="text-align:center; font-family: Helvetica">Agregat A</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa [min]</th>
            <th style="text-align:center; font-family: Helvetica">Napomena</th>                        
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">RECEX LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/recex-zakuca1a-006/">RecEx_ZAKUCA1A_006</a></td>
            <td style="text-align:center">02:13.056</td>
            <td style="text-align:center">Zapis odvajanja u otok. <br>Vremensko odstupanje originalnog zapisa od utvrđenog trenutka odvajanja:  <strong>-00:58:21.681</strong></td>
        </tr>
        <tr>
            <td style="text-align:center">WATCH LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1a-031/">Watch_ZAKUCA1A_031</a></td>
            <td style="text-align:center">01:49.757</td>
            <td style="text-align:center">Sinkronizacija na mrežu. <br>Odstupanje zapisa: <strong>19.407 sekundi</strong></td>                      
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}



{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica">Zapis</th>
            <th style="text-align:center; font-family: Helvetica">Agregat D</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa [min]</th>
            <th style="text-align:center; font-family: Helvetica">Napomena</th>                        
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">RECEX LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/recex-zakuca1d-002/">RecEx_ZAKUCA1D_002</a></td>
            <td style="text-align:center">02:13.056</td>
            <td style="text-align:center">Zapis odvajanja u otok. <br>Vremensko odstupanje zapisa od utvrđenog trenutka odvajanja: <strong>+00:15:17.654</strong></td>
        </tr>
        <tr>
            <td style="text-align:center">WATCH LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1d-022/">Watch_ZAKUCA1D_022</a></td>            
            <td style="text-align:center">04:30.850</td> 
            <td style="text-align:center">Sinkronizacija na mrežu. <br>Odstupanje zapisa: <strong>20.400 sekunde</strong></td>         
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}


{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica">Zapis</th>
            <th style="text-align:center; font-family: Helvetica">Agregat B</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa [min]</th>
            <th style="text-align:center; font-family: Helvetica">Napomena</th>            
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">RECEX LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/recex-zakuca1b-002/">RecEx_ZAKUCA1B_002</a></td>
            <td style="text-align:center">02:13.056</td>
            <td style="text-align:center">Zapis odvajanja u otok. <br>Vremensko odstupanje zapisa od utvrđenog trenutka odvajanja: <strong>-00:59:34.113</strong></td>
        </tr>
        <tr>
            <td style="text-align:center">WATCH LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1b-031/">Watch_ZAKUCA1B_031</a></td>            
            <td style="text-align:center">03:49.270</td>
            <td style="text-align:center">Sinkronizacija na mrežu. <br> Odstupanje zapisa: <strong>21.693 sekunde</strong></td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}



{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica">Zapis</th> 
            <th style="text-align:center; font-family: Helvetica">Agregat C</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa [min]</th>
            <th style="text-align:center; font-family: Helvetica">Napomena</th>             
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">WATCH LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1c-013/">Watch_ZAKUCA1C_013</a></td>            
            <td style="text-align:center">02:14.407</td>
            <td style="text-align:center">Zapis odvajanja u otok. <br>Vremensko odstupanje zapisa od utvrđenog trenutka odvajanja: <strong>00:00:21.360</strong></td>
        </tr>
        <tr>
            <td style="text-align:center"></td>            
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1c-022/">Watch_ZAKUCA1C_022</a></td>            
            <td style="text-align:center">00:46.877</td>
            <td style="text-align:center">Sinkronizacija na mrežu. <br>Odstupanje zapisa: <strong>43.235 sekundi</strong></td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}


{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica">Signal</th>
            <th style="text-align:center; font-family: Helvetica">Opis signala</th>
            <th style="text-align:center; font-family: Helvetica">Oznaka signala</th>
            <th style="text-align:center; font-family: Helvetica">Bazna vrijednost</th>
            <th style="text-align:center; font-family: Helvetica">Mjerna jedinica</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">VGACTINV, VGACT</td>
            <td style="text-align:center">Napon generatora</td>
            <td style="text-align:center">Ug</td>
            <td style="text-align:center">16.0</td>
            <td style="text-align:center">kV</td>            
        </tr>
        <tr>
            <td style="text-align:center">IGACTINV, IGACT</td>
            <td style="text-align:center">Struja generatora - inverz</td>
            <td style="text-align:center">Ig</td>
            <td style="text-align:center">5774.0</td>
            <td style="text-align:center">A</td>
        </tr>
        <tr>
            <td style="text-align:center">UFACT</td>
            <td style="text-align:center">Napon uzbude</td>
            <td style="text-align:center">Uf</td>
            <td style="text-align:center">74</td>
            <td style="text-align:center">V</td>            
        </tr>
        <tr>
            <td style="text-align:center">IFACT</td>
            <td style="text-align:center">Struja uzbude</td>
            <td style="text-align:center">If</td>
            <td style="text-align:center">725.0</td>
            <td style="text-align:center">A</td>
        </tr>
        <tr>
            <td style="text-align:center">PACT</td>
            <td style="text-align:center">Radna snaga generatora</td>
            <td style="text-align:center">Pg</td>
            <td style="text-align:center">160.0</td>
            <td style="text-align:center">MW</td>
        </tr>
        <tr>
            <td style="text-align:center">QACT</td>
            <td style="text-align:center">Jalova snaga generatora</td>
            <td style="text-align:center">Qg</td>
            <td style="text-align:center">160.0</td>
            <td style="text-align:center">MVAr</td>
        </tr>
        <tr>
            <td style="text-align:center">FGACT</td>
            <td style="text-align:center">Frekvencija</td>
            <td style="text-align:center">f</td>
            <td style="text-align:center">50.0</td>
            <td style="text-align:center">Hz</td>
        </tr>
        <tr>
            <td style="text-align:center">VGREF</td>
            <td style="text-align:center">Referenca Ug</td>
            <td style="text-align:center">Ug ref</td>
            <td style="text-align:center">1.0</td>
            <td style="text-align:center">p.u.</td>
        </tr>
        <tr>
            <td style="text-align:center">QCONRON1</td>
            <td style="text-align:center">Nalog za uključenje Q regulatora - logički signal</td>
            <td style="text-align:center">Q reg on</td>
            <td style="text-align:center">1.0</td>
            <td style="text-align:center">p.u.</td>
        </tr>
        <tr>
            <td style="text-align:center">QCONROF1</td>
            <td style="text-align:center">Nalog za isključenje Q regulatora - logički signal</td>
            <td style="text-align:center">Q reg off</td>
            <td style="text-align:center">1.0</td>
            <td style="text-align:center">p.u.</td>
        </tr>
        <tr>
            <td style="text-align:center">REFINC1, VRINC</td>
            <td style="text-align:center">Nalog za povećanje reference napona - logički signal</td>
            <td style="text-align:center">Vref VIŠE</td>
            <td style="text-align:center">1.0</td>
            <td style="text-align:center">p.u.</td>
        </tr>
        <tr>
            <td style="text-align:center">REFDEC1, VRDEC</td>
            <td style="text-align:center">Nalog za smanjenje reference napona - logički signal</td>
            <td style="text-align:center">Vref NIŽE</td>
            <td style="text-align:center">1.0</td>
            <td style="text-align:center">p.u.</td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}