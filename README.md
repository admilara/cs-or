# HE Zakučac – crni start i otočni rad

Obrada i vizualizacija mjernih podataka dostavljenih nakon pokusa **crnog starta** (03.12.2024.)
i **otočnog rada** (04.12.2024.) provedenih na sve četiri proizvodne jedinice (A, D, B i C) u GHE Zakučac.

**Stranica:** <https://admilara.github.io/cs-or/>

Stranica je izrađena u Jekyllu i objavljuje se putem GitHub Pages. Svaki izvor podataka ima
preglednu stranicu za pokus (crni start / otočni rad), a s nje se dolazi na pojedinačne stranice s interaktivnim
Plotly grafovima.

## Izvori podataka

| Izvor | Sadržaj | Crni start | Otočni rad |
| --- | --- | --- | --- |
| HOPS NM (MC Split) | Konzum po trafostanicama, mjesto odvajanja, naponi u TS Konjsko, položaj regulacijskih sklopki | – | `/or-hops-nm/` |
| HOPS WAMS | PMU mjerenja (#318, #323, #324) | `/cs-hops-wams/` | `/or-hops-wams/` |
| Končar KET – PROCIS | Mjerenja generatora, uzbude i turbine | `/cs-koncar-ket/` | `/or-koncar-ket/` |
| GEPPERT | Zapisi iz turbinskog regulatora | `/cs-geppert/` | `/or-geppert/` |
| Končar INEM | RecEx i Watch zapisi sustava uzbude | `/cs-uzbuda/` | `/or-uzbuda/` |

## Struktura repozitorija

```
_config.yml            postavke stranice + navigacija (header_sections)
_layouts/default.html  predložak svih stranica (zaglavlje, navigacija, podnožje)
assets/css/style.scss  stilovi
index.md               početna stranica
_pages/                Markdown stranice; svaka postaje /<ime-datoteke>/

konzum/                HOPS NM – konzum po TS (htmls/) i PROCIS crni start; Python skripte i CSV ulazi
mjesto_odvajanja/      HOPS NM – mjesto odvajanja (DV 110 kV Zakučac – Meterize II)
wams-cs/, wams-or/     HOPS WAMS – PMU grafovi za crni start / otočni rad
ket-or/                Končar PROCIS – otočni rad
turbinska/             GEPPERT – turbinski regulator
uzbuda/                Končar INEM – RecEx (cs/, or/) i Watch (watch/cs/, watch/or/) zapisi
```

Grafovi su samostalne HTML datoteke koje generiraju Python skripte u istim mapama
(pandas + Plotly). Stranice u `_pages/` ih ugrađuju preko `<iframe>`:

```html
<div class="wide-graph">
    <iframe src="{{ site.baseurl }}/turbinska/blackstart-agr-d-04.html" width="100%" height="800px" frameborder="0"></iframe>
</div>
```

Okvir `.wide-graph` koristi punu širinu prozora, a visina se automatski prilagođava sadržaju grafa.

## Dodavanje nove stranice

1. Generirati HTML graf odgovarajućom skriptom i spremiti ga u mapu izvora.
2. Dodati `_pages/<ime>.md` s `layout: default` i `title`, opisom i `<div class="wide-graph">` blokom.
3. Povezati stranicu s pripadne pregledne stranice (npr. `_pages/or-geppert.md`).
4. Novi izvor u navigaciji dodaje se u `header_sections` u `_config.yml`; isti popis gradi i kartice na početnoj
   stranici. Stavka s `available: false` prikazuje se kao neobjavljena, bez poveznice.

## Lokalni pregled

```bash
gem install bundler jekyll jekyll-seo-tag
jekyll serve --baseurl /cs-or
# http://localhost:4000/cs-or/
```

## Napomene

- Predlošci u Python skriptama u `<head>` dodaju `plotly-latest.min.js` (zamrznut na Plotly v1.58.5), a
  `pio.to_html(..., include_plotlyjs="cdn")` zatim učitava i Plotly 2.x. U objavljenim HTML datotekama koje
  učitavaju obje verzije suvišna je v1 oznaka uklonjena (grafove ionako iscrtava 2.x). Ako se grafovi ponovno
  generiraju, oznaka će se vratiti; to ne kvari prikaz, ali nepotrebno učitava oko 3,5 MB po grafu.
- Ulazni podaci (CSV, XLSX) nalaze se uz skripte koje ih obrađuju.
