# Gender Wage Gap — Data Mining Final Project

**Team:** Danis, Tastemir, Stanislav
**Problem:** quantify and explain the gender wage gap in US labor-market data.
**Dataset:** [Gender Pay Gap Dataset (Kaggle, fedesoriano)](https://www.kaggle.com/datasets/fedesoriano/gender-pay-gap-dataset) → `CurrentPopulationSurvey.csv` (download separately; not committed, see `.gitignore`).
**Russian version of this content:** [`README.ru.md`](README.ru.md).

This README is a glossary/index. Each task has its own file in [`docs/`](docs/) with
the full write-up (description + proposed/applied solution). Start with
[GPG-001](docs/GPG-001.md) if you are new to the project.

## Setup

```bash
# Python env with pandas, etc. — see your own venv / requirements
python -m venv .venv
.venv/Scripts/activate      # Windows
pip install pandas

# Download CurrentPopulationSurvey.csv from the Kaggle link above
# and place it in the repo root (it is gitignored).
```

## File Structure

```
.
├── README.md            # this file — glossary/index (English)
├── README.ru.md          # Russian version of the project write-up
├── CurrentPopulationSurvey.csv   # dataset (gitignored, download manually)
├── docs/                 # one file per task: description + solution
│   ├── GPG-001.md
│   ├── GPG-002.md
│   ├── GPG-003.md
│   ├── GPG-004.md
│   ├── GPG-005.md
│   ├── GPG-006.md
│   ├── GPG-007.md
│   ├── GPG-008.md
│   ├── GPG-009.md
│   ├── GPG-010.md
│   ├── GPG-011.md
│   ├── GPG-013.md
│   └── project-description/
│       └── description.md   # original assignment requirements (ex description.txt)
├── scripts/              # exploration / stats scripts used to derive docs numbers
    ├── explore_cps.py
    ├── explore_pandas.py
    └── wage_gap_stats.py
```

## Task Glossary

| Task | Title | Owner | Blocked by | Parallel with | Status | Doc |
|---|---|---|---|---|---|---|
| GPG-001 | Problem Definition & Research Questions | Danis | — (start here) | — | done | [docs/GPG-001.md](docs/GPG-001.md) |
| GPG-002 | Dataset Description | Danis | GPG-001 | GPG-003 | done | [docs/GPG-002.md](docs/GPG-002.md) |
| GPG-003 | Data Preprocessing | Tastemir (lead), Danis (design/review) | GPG-001 | GPG-002 | not started | [docs/GPG-003.md](docs/GPG-003.md) |
| GPG-004 | Exploratory Data Analysis (EDA) | Tastemir (lead), Stanislav (stat. tests) | GPG-003 | — | not started | [docs/GPG-004.md](docs/GPG-004.md) |
| GPG-005 | Feature Engineering | Danis + Stanislav | GPG-004 | — | not started | [docs/GPG-005.md](docs/GPG-005.md) |
| GPG-006 | Baseline Model | Stanislav | GPG-005 | — | not started | [docs/GPG-006.md](docs/GPG-006.md) |
| GPG-007 | Modeling (4+ models) | Stanislav (lead), Danis (code review) | GPG-006 | — | not started | [docs/GPG-007.md](docs/GPG-007.md) |
| GPG-008 | Model Evaluation & Tuning | Danis | GPG-007 | — | not started | [docs/GPG-008.md](docs/GPG-008.md) |
| GPG-009 | Results & Conclusions | Danis (lead), everyone contributes | GPG-008 | — | not started | [docs/GPG-009.md](docs/GPG-009.md) |
| GPG-010 | Slides (10–15 slides) | Tastemir (lead) | — | GPG-011 | not started | [docs/GPG-010.md](docs/GPG-010.md) |
| GPG-011 | Project Report (5–8 pages) | everyone together | — | GPG-010 | not started | [docs/GPG-011.md](docs/GPG-011.md) |
| GPG-012 | README + Reproducibility | Danis | — | — | in progress | this file (`README.md`) |
| GPG-013 | Contribution Statement | everyone together | GPG-012 | — | not started | [docs/GPG-013.md](docs/GPG-013.md) |

Run order generally follows the task IDs above (GPG-001 → … → GPG-013), except where the
"Parallel with" column marks two tasks that can run at the same time (GPG-002/GPG-003,
GPG-010/GPG-011).

## Key Facts (for quick reference)

- **Target variable:** `incwage` (annual wage) or `realhrwage` (real hourly wage,
  likely log-transformed) — see [GPG-002](docs/GPG-002.md#target-variable).
- **Key predictor:** `sex` / `female`.
- **Raw gender wage gap:** ~34% (mean `incwage`), ~31% (median `incwage`) — women
  earn less; gap persists on an hourly basis too.
- **Missing values:** concentrated in `citizen` (87%), `nativity` (25.5%), `educ99`
  (25.4%), `union` (12.3%); everything else is fully populated.
- **Project type:** regression (wage prediction), per assignment Part 2.A.
