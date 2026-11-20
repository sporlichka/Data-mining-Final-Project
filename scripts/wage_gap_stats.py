import csv
import sys
import statistics

path = sys.argv[1]

by_sex = {"1": [], "2": []}
by_sex_real = {"1": [], "2": []}
topcode_counts = {"1": 0, "2": 0}
zero_wage = {"1": 0, "2": 0}

with open(path, newline="", encoding="utf-8", errors="replace") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sex = row.get("sex")
        if sex not in by_sex:
            continue
        try:
            w = float(row["incwage"])
            by_sex[sex].append(w)
            if w == 0:
                zero_wage[sex] += 1
            if w >= 99999 or w in (999999, 999998):
                topcode_counts[sex] += 1
        except Exception:
            pass
        try:
            rw = row.get("realhrwage")
            if rw and rw != "NA":
                by_sex_real[sex].append(float(rw))
        except Exception:
            pass

for sex, label in [("1", "Male"), ("2", "Female")]:
    vals = by_sex[sex]
    vals_nz = [v for v in vals if v > 0]
    print(f"{label}: n={len(vals)}, mean_incwage={statistics.mean(vals):.0f}, "
          f"median_incwage={statistics.median(vals):.0f}, zero_wage={zero_wage[sex]} ({100*zero_wage[sex]/len(vals):.2f}%), "
          f"mean_incwage(nonzero)={statistics.mean(vals_nz):.0f}, "
          f"max={max(vals):.0f}, topcoded(>=99999)={topcode_counts[sex]}")
    rvals = by_sex_real[sex]
    if rvals:
        print(f"  realhrwage: n={len(rvals)}, mean={statistics.mean(rvals):.2f}, median={statistics.median(rvals):.2f}")

m_mean = statistics.mean(by_sex["1"])
f_mean = statistics.mean(by_sex["2"])
print(f"\nRaw gender wage gap (mean incwage): {100*(1 - f_mean/m_mean):.1f}% lower for women")
m_med = statistics.median(by_sex["1"])
f_med = statistics.median(by_sex["2"])
print(f"Raw gender wage gap (median incwage): {100*(1 - f_med/m_med):.1f}% lower for women")
