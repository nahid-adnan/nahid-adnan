# Hi, I'm Nahid 👋

**Data science postgrad at JCU (Cairns) — building toward a data analyst career in Australia.**

I came to data science from statistics. My MSc was in statistical theory and inference; the Master
of Data Science I'm finishing at James Cook University is where that turns into working software and
dashboards other people can actually use. The gap between "the analysis is correct" and "the analysis
is understood" is most of what I'm interested in.

This profile holds the work I'm learning from and building — Python, R, Power BI, SQL, and the
occasional experiment.

![Location](https://img.shields.io/badge/📍_Cairns,_QLD-Australia-2E8B57?style=flat-square)
[![MSc](https://img.shields.io/badge/🎓_MSc_Statistics-Jahangirnagar_University-4B8BBE?style=flat-square)](https://juniv.edu/)
[![MDS](https://img.shields.io/badge/📊_MDS-James_Cook_University-006747?style=flat-square)](https://www.jcu.edu.au/)
![Open to work](https://img.shields.io/badge/🎯_Open_to-Data_Analyst_roles-F2C811?style=flat-square)

---

## 🎓 Background

| | | |
|:--|:--|:--|
| 📊 **Master of Data Science** | James Cook University, Cairns | *in progress* |
| 📐 **MSc, Statistics** | Jahangirnagar University | completed |
| 🇦🇺 **Work rights** | 485 post-study work visa pathway | Brisbane-focused |

Statistics first, then the tooling. That order matters to how I work: I'd rather understand why a
number moved than produce a chart faster.

---

## 🧰 Tools I work with

**🔬 Analysis & programming**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

**📊 Visualisation & reporting**

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![DAX](https://img.shields.io/badge/DAX-01A88D?style=for-the-badge&logoColor=white)
![Power Query](https://img.shields.io/badge/Power%20Query-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

**⚙️ Workflow**

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)

---

## 🚀 What I'm doing now

- 📚 **Studying** data visualisation and data ethics at JCU — dashboard design theory, visual encoding, and the responsibilities that come with putting numbers in front of decision-makers
- 🐍 **Building** Python and analysis projects to sharpen the fundamentals — clean structure, readable logic, reproducible output
- 📊 **Publishing** Power BI work — two dashboards up, on Queensland schooling equity and the Tasmanian short-stay market
- 🎯 **Working toward** a data analyst role in Brisbane on a 485 visa

---

## 🔨 Selected work

| Project | What it is | Stack |
|:--|:--|:--|
| 📊 [**NAPLAN QLD equity dashboard**](https://github.com/nahid-adnan/naplan-qld-equity-dashboard) | Where are the equity gaps in Queensland schooling — 1,369 schools, 3 report pages | Power BI · DAX · Power Query |
| 🏝️ [**Tasmania short-stay dashboard**](https://github.com/nahid-adnan/Tasmania-short-stay-dashboard) | 5,293 listings, $145.3M revenue pool, 5 linked pages | Power BI · DAX |
| 🎮 [**blue-v-red**](https://github.com/nahid-adnan/blue-v-red) | Probabilistic CLI game that logs every round and analyses itself | Python · pandas · matplotlib |
| 🐍 [**cp5639-python-practicals**](https://github.com/nahid-adnan/cp5639-python-practicals) | Six practicals from conditionals to structured data | Pure Python 3 |
| ⌨️ [**cp1401-assignment-1**](https://github.com/nahid-adnan/cp1401-assignment-1) | Three Input-Process-Output programs | Pure Python 3 |

---

### 📊 [naplan-qld-equity-dashboard](https://github.com/nahid-adnan/naplan-qld-equity-dashboard)

An interactive **Power BI** dashboard asking where the equity gaps sit in Queensland schooling —
**1,369 schools** across three linked report pages, built on ACARA's 2014 NAPLAN release.

| | |
|:---|:---|
| ⭐ **Equity quadrants** | ICSEA-versus-score scatter with reference lines splitting schools four ways |
| 🗺️ **Point map** | Every school placed individually, because schools — not regions — are the unit of intervention |
| 🎗️ **Ribbon chart** | Whether sector rankings shift as students progress from Year 3 to Year 9 |
| 🌳 **Decomposition tree** | AI-assisted exploration of what drives score variation |

**The data work.** A **60,236-row** fact table unpivoted in Power Query from 44 result columns,
joined many-to-one to a 1,865-row school dimension on ACARA SML ID. Suppression codes are treated as
missing rather than zero, so an unreported school never renders as a poor performer — the single
decision that most changes what the dashboard says.

**The design work.** Encoding follows the Cleveland–McGill accuracy ranking, so anything needing
precise comparison uses position or length and never area alone. Layout follows Shneiderman's
*overview first, zoom and filter, details on demand*. Cross-visual interaction runs on a deliberate
three-tier policy — suppress, filter, or default highlight — rather than accepting Power BI's
defaults everywhere.

<sub>DAX measures · Power Query unpivot · star schema · drill-down · custom tooltip page · accessible theme</sub>

### 🏝️ [Tasmania-short-stay-dashboard](https://github.com/nahid-adnan/Tasmania-short-stay-dashboard)

An interactive **Power BI** dashboard on Tasmania's short-term rental market — **5,293 listings** and a
**$145.3M** estimated revenue pool across five linked report pages.

| | |
|:---|:---|
| 🗺️ **Geographic** | Bubble map of estimated 12-month revenue by local government area |
| 🎚️ **What-if** | Repricing scenario driven by a disconnected parameter table |
| ⭐ **Hosts** | Larger portfolios charge more but rate lower — the counter-intuitive finding |
| 🔎 **Drill-through** | Region → listing-level register with an adjustable quality bar |

<sub>DAX measures · what-if parameters · drill-through & drill-down · custom tooltip page · bookmarks</sub>

### 🎮 [blue-v-red](https://github.com/nahid-adnan/blue-v-red)

A turn-based command-line game where you build a Blue team and fight a computer-controlled Red team.
Each round is decided probabilistically by name length — `P(Blue wins) = len(blue) / (len(blue) + len(red))` —
and every round is logged to CSV so the outcomes can be analysed afterwards.

The built-in analysis module reads that log and produces **four charts**: a histogram of name lengths,
win rate by name length, predicted probability vs actual outcome, and cumulative win rate across all
rounds — turning a toy game into a small experiment in whether the model behaves as designed.

<sub>🐍 Python · 🐼 pandas · 🔢 NumPy · 📊 matplotlib · menu-driven CLI · CSV logging</sub>
<sub>Written under strict constraints: no global variables, no `while True`.</sub>

### 🐍 [cp5639-python-practicals](https://github.com/nahid-adnan/cp5639-python-practicals)

A portfolio of practicals from **CP5639 — Problem Solving and Programming**, working up from
decision logic to structured data across six practicals:

| | Focus |
|:---|:---|
| **P3** | Conditionals — eligibility checks, categorisers, fine calculators |
| **P4** | Loops & accumulation — sentinel loops, nested loops, sequence generators |
| **P5** | Menus & input validation |
| **P6** | Functions — modular design, constants, JCU grade converter |
| **P7** | Functions & debugging — BMI calculator, unit converters |
| **P8** | Lists & tuples — test-score analysis with grade and trend detection |

<sub>🐍 Pure Python 3, no external libraries · f-strings · docstrings · named constants</sub>

### ⌨️ [cp1401-assignment-1](https://github.com/nahid-adnan/cp1401-assignment-1)

Three programs from **CP1401 — Introduction to Programming**, each built around the
Input-Process-Output pattern:

- 🍕 **Pizza pay calculator** — driver pay from trips and minutes worked
- 🎾 **Tennis result** — match outcome plus an independent fast-match bonus check
- 😴 **Sleep tracker** — five nights of validated input, accumulating total sleep against a recommended target

<sub>🐍 Pure Python 3 · `for` and `while` loops · input validation · accumulation pattern</sub>

### 📈 More Power BI dashboards *(in progress)*

Further visualisation projects from my MDS, including an urban mobility dashboard and a
sustainable activewear sales analysis for North Queensland.

---

## 🧠 How I approach a dataset

- 🔍 **Understand the gaps before the numbers** — missing and suppressed values are decisions, not noise. Treating a suppressed result as zero quietly turns an unreported school into a failing one.
- 📐 **Encode for accuracy, not decoration** — position and length where a reader must compare precisely; colour and area only for secondary information.
- 🧾 **State the limitations on the page** — a dashboard that hides its own coverage problems isn't defensible when someone quotes it in a briefing.
- 🔁 **Build it so it can be rebuilt** — documented transformations, named measures, and a model someone else can open and follow.
- 🎯 **Design for the reader, not the analyst** — a time-poor officer should get something useful in the first five seconds, before touching a single filter.

---

## 📚 Coursework at JCU

| Subject | Focus |
|:--|:--|
| 📊 **MA5830** — Data Visualisation | Dashboard design theory, visual encoding, Power BI and Tableau |
| ⚖️ **CP5806** — Data Ethics | Privacy, breach case analysis, responsible data practice |
| 🐍 **CP5639** — Problem Solving & Programming | Python fundamentals through to structured data |
| 🧱 **CP5632 / CP1404** — Programming II | OOP, inheritance, file I/O, GUI development |
| ⌨️ **CP1401** — Introduction to Programming | Control flow, validation, the IPO pattern |

---

## 📊 Activity

![Python](https://img.shields.io/badge/Primary_language-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Dashboards-Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Repos](https://img.shields.io/badge/Public_repos-8-181717?style=flat-square&logo=github&logoColor=white)

- 🐍 Most of my current work is in **Python** — programming fundamentals and data analysis
- 📊 **Power BI** is where my visualisation coursework lands — two dashboards published, more coming
- 📉 Bringing **R** across from my statistics background as projects call for it
- 📁 Repos here range from coursework practicals to full analytical projects
- 🔄 Actively growing this profile each term

---

## 🌱 What I'm learning next

- 🧮 **Advanced DAX** — time intelligence and more complex measure patterns
- 🗄️ **SQL for analytics** — window functions and query optimisation
- 📐 **Statistical modelling in R** — carried over from my MSc
- ☁️ **Cloud data tools** — the next step once the fundamentals are solid

---

## 📬 Reach me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nahid-hasan-a8767114b)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:nahid34618@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nahid-adnan)

---

*Based in Cairns, Queensland 🇦🇺 | Open to data analyst opportunities in Brisbane*
