---
layout: default
title: Navigacija
description: Navigacijska stranica za rezultate obrade
---

# Obrada rezultata

Ovo je navigacijska stranica za rezultate obrade dostavljenih podataka nakon pokusa
crnog starta i otočnog rada koji su provedeni na sve četiri proizvodne jedinice A, D, B i C u GHE Zakučac
03.12. i 04.12.2024. Hyperlinkovi vode na grafove prema podatcima koji su navedeni. 

## 03.12.2024. Crni start

### Podatci: Končar KET - PROCIS
Za svaki pokus crnog starta grafički su prikazane sljedeće mjerne veličine:
* Radna snaga generatora P [MW\]
* Jalova snaga generatora Q [Mvar\]
* Naponi generatora UL1L2, UL2L3, UL3L1 \[V\]
* Struje generatora IL1, IL2, IL3 \[A\]
* Napon i struja uzbude Uf, If
* Brzina vrtnje, zadana brzina vrtnje, frekvencija \[%\]
* Frekvencija f \[Hz\]
* Otvor privodnog kola y \[%]
* Tlak u spirali turbine i tlak u tlačnom cjevovodu p \[bar\]


1. Crni start - proizvodna jedinica A - [rezultati]({{ site.baseurl }}/procis-cs-gen-a/)
2. Crni start - proizvodna jedinica D - [rezultati]({{ site.baseurl }}/procis-cs-gen-d/)
3. Crni start - proizvodna jedinica B - [rezultati]({{ site.baseurl }}/procis-cs-gen-b/)
4. Crni start - proizvodna jedinica C - [rezultati]({{ site.baseurl }}/procis-cs-gen-c/)

## 04.12.2024. Otočni rad

### Podatci: Končar KET - PROCIS
Za svaki pokus otočnog rada grafički su prikazane sljedeće mjerne veličine:
* Radna snaga generatora P [MW\]
* Jalova snaga generatora Q [Mvar\]
* Naponi generatora UL1L2, UL2L3, UL3L1 \[V\]
* Struje generatora IL1, IL2, IL3 \[A\]
* Napon i struja uzbude Uf, If 
* Brzina vrtnje, zadana brzina vrtnje, frekvencija \[%\]
* Frekvencija f \[Hz\]
* Otvor privodnog kola y \[%]
* Tlak u spirali turbine i tlak u tlačnom cjevovodu p \[bar\]
* Protok u tlačnom cjevovodu \[m³/s]

1. Otočni rad - proizvodna jedinica A - [rezultati]({{ site.baseurl }}/procis-or-gen-a/)
2. Otočni rad - proizvodna jedinica D - [rezultati]({{ site.baseurl }}/procis-or-gen-d/)
3. Otočni rad - proizvodna jedinica B - [rezultati]({{ site.baseurl }}/procis-or-gen-b/)
4. Otočni rad - proizvodna jedinica C - [rezultati]({{ site.baseurl }}/procis-or-gen-c/)

### Podatci: HOPS NM - konzum
Dostupne su mjerne veličine P, Q, I, U i položaj regulacijske sklopke. 
Ovisno o stanici mjerenja snage su ili na 110 kV ili na 35 kV naponskoj razini.

Dostavljeni su podatci mjerenja svih trafostanica koje su bile uključene u pokuse otočnog rada, vizualizacija je dana za sva četiri agregata.
 
* TS HE Zakučac - TR1
    * [GEN A - OR]({{ site.baseurl }}/ts-zakucac-or-gen-a/)
    * [GEN D - OR]({{ site.baseurl }}/ts-zakucac-or-gen-d/)
    * [GEN B - OR]({{ site.baseurl }}/ts-zakucac-or-gen-b/)
    * [GEN C - OR]({{ site.baseurl }}/ts-zakucac-or-gen-c/)     
* TS Kaštela - TR2 
    * [GEN A - OR]({{ site.baseurl }}/ts-kastela-tr2-or-gen-a/)
    * [GEN D - OR]({{ site.baseurl }}/ts-kastela-tr2-or-gen-d/)
    * [GEN B - OR]({{ site.baseurl }}/ts-kastela-tr2-or-gen-b/)
    * [GEN C - OR]({{ site.baseurl }}/ts-kastela-tr2-or-gen-c/)
* TS Sinj - TR1 i TR2
    * [GEN A - OR]({{ site.baseurl }}/ts-sinj-or-gen-a/)
    * [GEN D - OR]({{ site.baseurl }}/ts-sinj-or-gen-d/)
    * [GEN B - OR]({{ site.baseurl }}/ts-sinj-or-gen-b/)
    * [GEN C - OR]({{ site.baseurl }}/ts-sinj-or-gen-c/)
* TS Dugopolje - TR1 i TR2
    * [GEN A - OR]({{ site.baseurl }}/ts-dugopolje-or-gen-a/)
    * [GEN D - OR]({{ site.baseurl }}/ts-dugopolje-or-gen-d/)
    * [GEN B - OR]({{ site.baseurl }}/ts-dugopolje-or-gen-b/)
    * [GEN C - OR]({{ site.baseurl }}/ts-dugopolje-or-gen-c/)
* TS Meterize - TR1 i TR2
    * [GEN A - OR]({{ site.baseurl }}/ts-meterize-or-gen-a/)
    * [GEN D - OR]({{ site.baseurl }}/ts-meterize-or-gen-d/)
    * [GEN B - OR]({{ site.baseurl }}/ts-meterize-or-gen-b/)
    * [GEN C - OR]({{ site.baseurl }}/ts-meterize-or-gen-c/)
* TS Vrboran - TR1 i TR2
    * [GEN A - OR]({{ site.baseurl }}/ts-vrboran-or-gen-a/)
    * [GEN D - OR]({{ site.baseurl }}/ts-vrboran-or-gen-d/)
    * [GEN B - OR]({{ site.baseurl }}/ts-vrboran-or-gen-b/)
    * [GEN C - OR]({{ site.baseurl }}/ts-vrboran-or-gen-c/)

Kako bi se snaga proizvodnje pojedinih agregata usporedila s konzumom u otoku, 
dana je sumarna karakteristika radne i jalove snage konzuma u trafostanicama u otoku.
Grafovi prikazuju odvojeno radnu snagu i jalovu snagu za svaki pojedini agregat.

* Sumarna karakteristika - [rezultati]({{ site.baseurl }}/suma-konzum-or/)

#### HOPS NM - mjesta odvajanja

Mjesto odvajanja za sva četiri pokusa otočnog rada bio je DV 110 kV HE Zakučac - Meterize II.
Na mjestu odvajanja, s obje strane dalekovoda, mjerene su sljedeće veličine:
* Struja I [A\]
* Radna snaga P [MW\]
* Jalova snaga Q \[Mvar\]
* Napon U \[kV\]

Rezultati su prikazani odvojeno za sva četiri agregata:
* [GEN A - MJESTO ODVAJANJA]({{ site.baseurl }}/mjesto-odvajanja-gen-a/)
* [GEN D - MJESTO ODVAJANJA]({{ site.baseurl }}/mjesto-odvajanja-gen-d/)
* [GEN B - MJESTO ODVAJANJA]({{ site.baseurl }}/mjesto-odvajanja-gen-b/)
* [GEN C - MJESTO ODVAJANJA]({{ site.baseurl }}/mjesto-odvajanja-gen-c/)


#### HOPS - WAMS PODATCI

Od strane HOPS-a dostavljeni su i podatci za četiri PMU-a za četiri promatrana perioda - po 
jedan za svaki obavljeni pokus otočnog rada. Vizualizacije su dostupne na hyperlinkovima ispod.
* 24-12-04-0812_to_24-12-04-0921_v2.1.2975.csv - otočni rad agregata A
* 24-12-04-1048_to_24-12-04-1147_v2.1.2975.csv - otočni rad agregata D
* 24-12-04-1324_to_24-12-04-1426_v2.1.2975.csv - otočni rad agregata B
* 24-12-04-1527_to_24-12-04-1603_v2.1.2975.csv - otočni rad agregata C

Četiri dostupna PMU-a su:
* **PMU #14** = RHE VEL VP 400 KONJ
* **PMU #318** = HE ZAK VP 220 KONJ
* **PMU #323** = HE ZAK 110 GEN 4 (D)
* **PMU #324** = HE ZAK 220 GEN 2 (B)

Za sva četiri agregata promatran je PMU #318, koji se nalazi u VP 220 kV Konjsko - Zakučac.
Od generatora u HE Zakučac, PMU je ugrađen na generatore B (220 kV) i D (110 kV) te je za otočni rad
ta dva agregata dostupna i vizualizacija njihovih pripadajućih PMU-ova.


| Agregat | Rezultati                                                |
| :------ |:-------------------------------------------------------: | 
|Agregat A| [A - PMU#318]({{ site.baseurl }}/or-agregata-a-pmu#318/) |
|Agregat D| [D - PMU#318]({{ site.baseurl }}/or-agregata-d-pmu#318/) |
|         | [D - PMU#323]({{ site.baseurl }}/or-agregata-d-pmu#323/) |
|Agregat B| [B - PMU#318]({{ site.baseurl }}/or-agregata-b-pmu#318/) |
|         | [B - PMU#324]({{ site.baseurl }}/or-agregata-b-pmu#324/) |
|Agregat C| [C - PMU#318]({{ site.baseurl }}/or-agregata-c-pmu#318/) |

