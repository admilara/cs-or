---
layout: default
title: OTOČNI RAD - REZULTATI HOPS NM
description: Kratki pregled podataka dostavljenih iz MC Split za pokuse otočnog rada u HE Zakučac
---
<style scoped>
table {
  font-size: 13px;
}
</style>
<h1 style="text-align: center; font-family: Helvetica; color: blue">04.12.2024. Otočni rad</h1>

<h2 style="text-align: center; font-family: Helvetica; color: blue">Podatci: HOPS NM - konzum</h2>

Dostupne su mjerne veličine P, Q, I, U i položaj regulacijske sklopke. 
Ovisno o stanici mjerenja snage su ili na 110 kV ili na 35 kV naponskoj razini.

Dostavljeni su podatci mjerenja svih trafostanica koje su bile uključene u pokuse otočnog rada, vizualizacija je dana za sva četiri agregata.


{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center">TS HE Zakučac - TR1</th>
            <th style="text-align:center">TS Kaštela - TR2</th>
            <th style="text-align:center">TS Sinj - TR1 i TR2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-zakucac-or-gen-a/">GEN A - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-kastela-tr2-or-gen-a/">GEN A - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-sinj-or-gen-a/">GEN A - OR</a></td>
        </tr>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-zakucac-or-gen-d/">GEN D - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-kastela-tr2-or-gen-d/">GEN D - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-sinj-or-gen-d/">GEN D - OR</a></td>
        </tr>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-zakucac-or-gen-b/">GEN B - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-kastela-tr2-or-gen-b/">GEN B - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-sinj-or-gen-b/">GEN B - OR</a></td>
        </tr>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-zakucac-or-gen-c/">GEN C - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-kastela-tr2-or-gen-c/">GEN C - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-sinj-or-gen-c/">GEN C - OR</a></td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th style="text-align:center">TS Dugopolje - TR1 i TR2</th>
            <th style="text-align:center">TS Meterize - TR1 i TR2</th>
            <th style="text-align:center">TS Vrboran - TR1 i TR2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-dugopolje-or-gen-a/">GEN A - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-meterize-or-gen-a/">GEN A - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-vrboran-or-gen-a/">GEN A - OR</a></td>
        </tr>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-dugopolje-or-gen-d/">GEN D - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-meterize-or-gen-d/">GEN D - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-vrboran-or-gen-d/">GEN D - OR</a></td>
        </tr>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-dugopolje-or-gen-b/">GEN B - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-meterize-or-gen-b/">GEN B - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-vrboran-or-gen-b/">GEN B - OR</a></td>
        </tr>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-dugopolje-or-gen-c/">GEN C - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-meterize-or-gen-c/">GEN C - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-vrboran-or-gen-c/">GEN C - OR</a></td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}


Kako bi se snaga proizvodnje pojedinih agregata usporedila s konzumom u otoku, 
dana je sumarna karakteristika radne i jalove snage konzuma u trafostanicama u otoku.
Grafovi prikazuju odvojeno radnu snagu i jalovu snagu za svaki pojedini agregat.

* **Sumarna karakteristika** - [rezultati]({{ site.baseurl }}/suma-konzum-or/)


<h2 style="text-align: center; font-family: Helvetica; color: blue">Podatci: HOPS NM - mjesta odvajanja</h2>

Mjesto odvajanja za sva četiri pokusa otočnog rada bio je DV 110 kV HE Zakučac - Meterize II.
Na mjestu odvajanja, s obje strane dalekovoda, mjerene su sljedeće veličine:

{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:left"></th>
            <th style="text-align:center">Oznaka</th>
            <th style="text-align:center">Mjerna jedinica</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:left">Struja</td>
            <td style="text-align:center">I</td>
            <td style="text-align:center">[A]</td>
        </tr>
        <tr>
            <td style="text-align:left">Radna snaga</td>
            <td style="text-align:center">P</td>
            <td style="text-align:center">[MW]</td>
        </tr>
        <tr>
            <td style="text-align:left">Jalova snaga</td>
            <td style="text-align:center">Q</td>
            <td style="text-align:center">[Mvar]</td>
        </tr>
        <tr>
            <td style="text-align:left">Napon</td>
            <td style="text-align:center">U</td>
            <td style="text-align:center">[kV]</td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}

Rezultati su prikazani odvojeno za sva četiri agregata:
* [GEN A - MJESTO ODVAJANJA]({{ site.baseurl }}/mjesto-odvajanja-gen-a/)
* [GEN D - MJESTO ODVAJANJA]({{ site.baseurl }}/mjesto-odvajanja-gen-d/)
* [GEN B - MJESTO ODVAJANJA]({{ site.baseurl }}/mjesto-odvajanja-gen-b/)
* [GEN C - MJESTO ODVAJANJA]({{ site.baseurl }}/mjesto-odvajanja-gen-c/)