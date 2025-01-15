---
layout: default
title: OTOČNI RAD - VELIČINE IZ TURBINSKOG REGULATORA
description: Kratki pregled podataka iz turbinskog za pokuse otočnog rada u HE Zakučac
---

<h1 style="text-align: center; font-family: Helvetica; color: blue">04.12.2024. Otočni rad</h1>

<h2 style="text-align: center; font-family: Helvetica; color: blue">Podatci: GEPPERT</h2>

Od strane GEPPERT-a dostavljeni su zapisi iz turbinskog regulatora za pokuse otočnog rada agregata A, D, B i C.
Različit broj zapisa je dan ovisno o generatoru, ali za sve je dana vizualizacija. 

Za pokuse otočnog rada agregata A ne postoji zapis u kojem je vidljiv sam trenutak odvajanja zbog grešaka u koordinaciji prilikom izvedenog pokusa.
Trenutak odvajanja nastupio je prije nego je GEPPERT bio spreman za odvajanje. 

{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica; color: blue">Agregat</th>
            <th style="text-align:center; font-family: Helvetica; color: blue">Datoteka</th>
            <th style="text-align:center; font-family: Helvetica; color: blue">Napomena</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">Agregat A</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/snimanjeislandmode-agr-a-001-08-57-pocetak-000-00/">snimanjeislandmode-agr-a-001-08-57-pocetak-000-00</a></td>
            <td style="text-align:center">Testiranje, od 08:33:50.0 do 08:57:47.2</td>
        </tr>
        <tr>
            <td style="text-align:center"></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/snimanjeislandmode-agr-a-001-09-00-pocetak-000-00/">snimanjeislandmode-agr-a-001-09-00-pocetak-000-00</a></td>
            <td style="text-align:center">Testiranje, od 09:00:19.5 do 09:00:39.0</td>
        </tr>
        <tr>
            <td style="text-align:center"></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/snimanjeislandmode-agr-a-001-09-16-pocetak-000-00/">snimanjeislandmode-agr-a-001-09-16-pocetak-000-00</a></td>
            <td style="text-align:center">Testiranje, od 09:13:54.4 do 09:16:19.9</td>
        </tr>
        <tr>
            <td style="text-align:center"></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/snimanjeislandmode-agr-a-001-09-16-pocetak-000/">snimanjeislandmode-agr-a-001-09-16-pocetak-000</a></td>
            <td style="text-align:center">Pokus otočnog rada, od 09:16:50.3 do 10:23:11.5</td>
        </tr>
        <tr>
            <td style="text-align:center"></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/snimanjeislandmode-agr-a-001-09-16-pocetak-001/">snimanjeislandmode-agr-a-001-09-16-pocetak-001</a></td>
            <td style="text-align:center">Testiranje, od 10:25:09.6 do 10:26:26.4</td>
        </tr>
        <tr>
            <td style="text-align:center">Agregat D</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/snimanjeislandmode-agr-d-001-11-00-pocetak-000/">snimanjeislandmode-agr-d-001-11-00-pocetak-000</a></td>
            <td style="text-align:center">Testiranje, od 10:30:15.5 do 10:58:42.1</td>
        </tr>
        <tr>
            <td style="text-align:center"></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/snimanjeislandmode-agr-d-001-11-00-pocetak-001/">snimanjeislandmode-agr-d-001-11-00-pocetak-001</a></td>
            <td style="text-align:center">Pokus otočnog rada, od 10:59:24.3 do 12:51:13.6</td>
        </tr> 
        <tr>
            <td style="text-align:center">Agregat B</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/snimanjeislandmode-agr-b-001-11-00-pocetak-000/">snimanjeislandmode-agr-b-001-11-00-pocetak-000</a></td>
            <td style="text-align:center">Pokus otočnog rada, od 14:15:44.7 do 15:32:54.0</td>
        </tr> 
        <tr>
            <td style="text-align:center">Agregat C</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/snimanjeislandmode-agr-c-001-11-00-pocetak-000/">snimanjeislandmode-agr-c-001-11-00-pocetak-000</a></td>
            <td style="text-align:center">Pokus otočnog rada, od 15:40:19.4 do 17:10:18.3</td>
        </tr>        
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}
