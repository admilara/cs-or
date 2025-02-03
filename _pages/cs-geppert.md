---
layout: default
title: CRNI START - VELIČINE IZ TURBINSKOG REGULATORA
description: Kratki pregled podataka iz turbinskog za pokuse otočnog rada u HE Zakučac
---


<h1 style="text-align: center; font-family: Helvetica; color: red">03.12.2024. Crni start</h1>

<h2 style="text-align: center; font-family: Helvetica; color: red">Podatci: GEPPERT</h2>

Od strane GEPPERT-a dostavljeni su zapisi iz turbinskog regulatora za pokuse crnog starta agregata A, D, B i C.
Prikazani su samo zapisi koji prikazuju sam pokus, testni zapisi nisu prikazani. 

{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica; color: white">Agregat</th>
            <th style="text-align:center; font-family: Helvetica; color: white">Datoteka</th>
            <th style="text-align:center; font-family: Helvetica; color: white">Napomena</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">Agregat A</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/blackstart-agr-a-02/">blackstart-agr-a-02</a></td>
            <td style="text-align:center">Pokus crnog starta, zapis od 09:37:40.6 do 10:37:51.0</td>
        </tr>
        <tr>
            <td style="text-align:center">Agregat D</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/blackstart-agr-d-04/">blackstart-agr-d-04</a></td>
            <td style="text-align:center">Pokus crnog starta, od 11:37:26.5 do 12:23:39.9</td>
        </tr>
        <tr>
            <td style="text-align:center">Agregat B</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/blackstart-agr-b-02/">blackstart-agr-b-02</a></td>
            <td style="text-align:center">Pokus crnog starta, od 14:02:05.2 do 15:18:00.9</td>
        </tr> 
        <tr>
            <td style="text-align:center">Agregat C</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/blackstart-agr-c-01/">blackstart-agr-c-01</a></td>
            <td style="text-align:center">Pokus crnog starta, od 15:26:29.7 do 16:21:59.6</td>
        </tr>        
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}


{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica; color: white">Ime signala</th>
            <th style="text-align:center; font-family: Helvetica; color: white">Oznaka</th>
            <th style="text-align:center; font-family: Helvetica; color: white">Veličina</th>
            <th style="text-align:center; font-family: Helvetica; color: white">Opis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">00_speed_setpoint</td>
            <td style="text-align:center">n set</td>
            <td style="text-align:center">%</td>
            <td style="text-align:center">Setpoint brzine vrtnje</td>
        </tr>
        <tr>
            <td style="text-align:center">01_opening_sp</td>
            <td style="text-align:center">y set</td>
            <td style="text-align:center">%</td>
            <td style="text-align:center">Setpoint otvora privodnog kola</td>
        </tr>
        <tr>
            <td style="text-align:center">02_gate_servo_feedback</td>
            <td style="text-align:center">y</td>
            <td style="text-align:center">%</td>
            <td style="text-align:center">Feedback servo motora za otvaranje privodnog kola</td>
        </tr>
        <tr>
            <td style="text-align:center">03_power_sp</td>
            <td style="text-align:center">P</td>
            <td style="text-align:center">MW</td>
            <td style="text-align:center">Setpoint radne snage generatora</td>
        </tr>
        <tr>
            <td style="text-align:center">04_actual_opening</td>
            <td style="text-align:center">y act</td>
            <td style="text-align:center">%</td>
            <td style="text-align:center">Otvor privodnog kola</td>
        </tr>
        <tr>
            <td style="text-align:center">05_actual_power</td>
            <td style="text-align:center">P act</td>
            <td style="text-align:center">MW</td>
            <td style="text-align:center">Radna snaga generatora</td>
        </tr>
        <tr>
            <td style="text-align:center">06_power_pid_out</td>
            <td style="text-align:center">P pid</td>
            <td style="text-align:center">%</td>
            <td style="text-align:center">Signal regulatora - radna snaga na izlazu regulatora</td>
        </tr>
        <tr>
            <td style="text-align:center">07_power_pid_fwd_o</td>
            <td style="text-align:center">P pid fwd</td>
            <td style="text-align:center">%</td>
            <td style="text-align:center">Signal regulatora - radna snaga koja se prosljeđuje</td>
        </tr>
        <tr>
            <td style="text-align:center">08_speed_pidout</td>
            <td style="text-align:center">n pid out</td>
            <td style="text-align:center">%</td>
            <td style="text-align:center">Signal regulatora - brzina vrtnje na izlazu iz regulatora</td>
        </tr>
        <tr>
            <td style="text-align:center">09_actual_head</td>
            <td style="text-align:center">h</td>
            <td style="text-align:center">m</td>
            <td style="text-align:center">Pad</td>
        </tr>
        <tr>
            <td style="text-align:center">10_grid_freq</td>
            <td style="text-align:center">f</td>
            <td style="text-align:center">Hz</td>
            <td style="text-align:center">Mrežna frekvencija</td>
        </tr>
        <tr>
            <td style="text-align:center">11_blackstart_on</td>
            <td style="text-align:center">CS</td>
            <td style="text-align:center">pu</td>
            <td style="text-align:center">Signal crnog starta</td>
        </tr>
        <tr>
            <td style="text-align:center">13_actual_speed</td>
            <td style="text-align:center">n</td>
            <td style="text-align:center">%</td>
            <td style="text-align:center">Brzina vrtnje</td>
        </tr>
        <tr>
            <td style="text-align:center">15_remote_speed_sp</td>
            <td style="text-align:center">n</td>
            <td style="text-align:center">%</td>
            <td style="text-align:center">Setpoint brzine vrtnje - remote</td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}
