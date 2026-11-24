# GPG-004 — auto-generated findings (from `notebooks/GPG-004_eda.ipynb`)

## Conclusions

1. **The raw gender wage gap is substantial and persists on an hourly basis.** On a weighted basis women earn 22.8% less per hour than men in geometric-mean terms (24.3% at the median). On annual wage income the gap is 32.8% (mean) / 28.6% (median). Because the hourly gap is smaller than the annual gap, part of the annual gap comes from fewer hours/weeks, but the remainder is not explained by hours alone (RQ1).

2. **The gap narrowed between 1981 and 2013.** The weighted geometric-mean gap averaged 33.5% in the first 2 survey years and 17.9% in the last 2; the linear trend is -0.61 percentage points per year (R² = 0.97, p = 6.78e-05) (RQ1).

3. **Wages are strongly right-skewed — the log of the hourly wage is a better target.** Skewness of the hourly wage is 572.48 versus 0.08 for ln(wage). The log target is much closer to symmetric, and regression coefficients on it read as approximate percentage differences.

4. **edu_group and adj_occ2name are the categorical factors that separate wages most.** One-way ANOVA (η² = share of variance in ln wage explained): edu_group η² = 0.164; adj_occ2name η² = 0.129; race η² = 0.036. For comparison, sex alone has η² = 0.052 (Cohen's d = 0.47). Kruskal–Wallis gives the same ranking. Tukey HSD: all pairs of education groups differ significantly (RQ4).

5. **Men and women are distributed very unevenly across occupations; occupations with more women pay more.** χ² test of sex × occupation: Cramér's V = 0.46 (p < 1e-300); the Spearman correlation between an occupation's female share and its median hourly wage is ρ = 0.17. Occupational segregation is therefore a candidate explanation of part of the gap (RQ2).

6. **The gap grows with career length.** The raw gap is 7.3% for workers with 0–4 years of potential experience and 28.3% at 25–29 years. Wage profiles of men rise more steeply with experience than those of women (Figure 8) (RQ2/RQ4).

7. **More education raises wages for both sexes, but a gap remains at every education level.** Median-wage gap by education: Below bachelor's 26%, Bachelor's 23%, Advanced degree 23%. The two-way ANOVA interaction sex × education is significant (p 1.38e-30), i.e. the gap differs by education level (partial η² of the interaction = 0.0004).

8. **Observable characteristics explain part of the gap, and sex remains a significant predictor.** The OLS coefficient on `female` moves from -0.277 (raw, 24.2% less) to -0.240 (21.4% less) after controlling for year, education, experience, hours, occupation, region, race and marital status. The controls account for roughly 13% of the raw log gap; the remaining 87% is unexplained by these variables (p < 1e-300). This is consistent with RQ3. It is a statistical association, not proof of discrimination, since unobserved factors may matter (RQ2/RQ3).

9. **Which features carry the linear signal.** Strongest numeric correlates of ln wage: education (r = +0.40), weekly hrs (r = +0.15), age (r = +0.13). Strongest binary features: lehs (r = -0.39), foodcare (r = -0.22), manager (r = +0.22). `female` itself correlates r = -0.23 with the log wage (RQ4).

10. **Data caveats: top-coding and very large N.** 0.4% of men versus 0.0% of women are at the CPS top-code; because of this censoring the measured gap is probably understated. With ~344k observations tiny differences become 'statistically significant', so conclusions rely on effect sizes (d, η², Cramér's V, coefficient size) rather than p-values alone. The Mincer regression is descriptive and omits unobservables (e.g. job tenure, career interruptions).

11. **Occupation is only partly captured by `adj_occ2name`.** 39% of workers fall into the catch-all group 'Other' (the source field is empty for them; this group contains e.g. sales, education, healthcare and food-service jobs and is 62% female). Occupational segregation and the share of the gap explained by occupation are therefore understated; a finer occupation variable (from `occ1990` or the occupation dummies) is planned in GPG-005 (RQ2).

## Key statistical tests

- Welch t-test (ln wage, men vs women): t = 137.6, p < 1e-300; Mann–Whitney p < 1e-300; Cohen's d = 0.469
- One-way ANOVA (η² per factor):

  | Factor | groups | F | η² | p |
  |---|---|---|---|---|
  | edu_group | 3 | 33,696 | 0.164 | < 1e-300 |
  | adj_occ2name | 13 | 4,252 | 0.129 | < 1e-300 |
  | sex_label | 2 | 18,932 | 0.052 | < 1e-300 |
  | race | 4 | 4,314 | 0.036 | < 1e-300 |
  | marst | 6 | 1,755 | 0.025 | < 1e-300 |
  | year | 7 | 1,070 | 0.018 | < 1e-300 |
  | classwkr | 7 | 867 | 0.015 | < 1e-300 |
  | region | 9 | 598 | 0.014 | < 1e-300 |

- Two-way ANOVA sex × education interaction: p 1.38e-30
- χ² sex × occupation: Cramér's V = 0.456

## OLS preview: `female` coefficient as controls are added

| Model | R² | female coef | women earn less |
|---|---|---|---|
| M0 raw (sex only) | 0.052 | -0.277 | 24.2% |
| M1 + survey year | 0.072 | -0.282 | 24.6% |
| M2 + education & experience | 0.251 | -0.285 | 24.8% |
| M3 + hours & weeks | 0.257 | -0.267 | 23.4% |
| M4 + occupation & region | 0.313 | -0.245 | 21.7% |
| M5 + race & marital status | 0.335 | -0.240 | 21.4% |

## Figures (`docs/figures/GPG-004/`)

- `01_wage_distribution.png`
- `02_numeric_distributions.png`
- `03_composition_education_occupation.png`
- `04_correlation_matrix.png`
- `05_top_binary_correlations.png`
- `06_gap_over_time.png`
- `07_wage_by_education_sex.png`
- `08_experience_profile_and_gap.png`
- `09_occupational_segregation.png`
- `10_gap_with_controls.png`
