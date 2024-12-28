---
layout: default
title: WAMS rezultati - PMU#324 - AGREGAT B
---

## WAMS - PMU #324 - Agregat B 

#### Otočni rad

Na grafovima ispod prikazana su mjerenja s PMU-a **#324** koji se nalazi na **GEN B (220 kV) u HE Zakučac** za period unutar
kojeg je proveden pokus otočnog rada agregata B u GHE Zakučac.

Sve veličine su preuzete iz dostavljenog csv-a `24-12-04-1324_to_24-12-04-1426_v2.1.2975.csv`.

Vrijeme detekcije OR preuzeto je iz Liste KDR za Regiju Split, koja je dostavljena od strane MC Split.
Prema informacijama HOPS MC Split, GPS nije pouzdan - odstupanje iznosi 7 sekundi, što je vidljivo iz grafova i zabilježenog
vremena prema listi KRD.

<style scoped>
table {
  font-size: 13px;
}
</style>

| Agregat | Vrijeme detekcije OR |  Lokacija             | Vrijeme sinkronizacije | Lokacija          |
| :------ | :------------------: | :------------------:  | :---------------------:|:-----------------:|
|Agregat B| 2024-12-04 14:24:28  | HE ZAK 110 METERIZE/2 | 2024-12-04 15:25:27    | HE ZAK 110 SP W12 |

Iz dostavljene csv datoteke preuzete su veličine:
* PMU#324 &#124;IN&#124; magn [A]
* PMU#324 &#124;UN&#124; magn [pu]
* PMU#324 f(PMU) [Hz]
* PMU#324 P [W]
* PMU#324 Q [VAr]

<div class="wide-graph">
    <iframe src="{{ site.baseurl }}/wams-or/or-agregata-b-pmu-324.html" width="100%" height="800px" frameborder="0"></iframe>
</div>