import csv
import sys
from collections import Counter

path = sys.argv[1]

cols_of_interest = ["year","sex","age","race","marst","educ99","empstat","labforce",
                     "classwkr","wkswork1","uhrswork","incwage","hrwage","realhrwage",
                     "female","union","citizen","nativity","hispan"]

counters = {c: Counter() for c in ["year","sex","race","marst","educ99","empstat","labforce","classwkr","union","female"]}
na_counts = Counter()
total = 0
incwage_vals = []
age_vals = []
min_year, max_year = None, None

with open(path, newline="", encoding="utf-8", errors="replace") as f:
    reader = csv.DictReader(f)
    n_features = len(reader.fieldnames)
    for row in reader:
        total += 1
        for c in cols_of_interest:
            v = row.get(c, "")
            if v == "NA" or v == "" :
                na_counts[c] += 1
        for c in counters:
            counters[c][row.get(c, "")] += 1
        try:
            y = int(row["year"])
            if min_year is None or y < min_year: min_year = y
            if max_year is None or y > max_year: max_year = y
        except Exception:
            pass
        if total % 50000 == 0:
            print(f"...{total} rows processed", file=sys.stderr)

print("n_features (columns):", n_features)
print("total_rows:", total)
print("year_range:", min_year, "-", max_year)
print()
for c in cols_of_interest:
    print(f"NA/missing in {c}: {na_counts[c]} ({100*na_counts[c]/total:.2f}%)")
print()
for c in counters:
    print(f"--- {c} top values ---")
    for val, cnt in counters[c].most_common(10):
        print(f"  {val!r}: {cnt} ({100*cnt/total:.2f}%)")
