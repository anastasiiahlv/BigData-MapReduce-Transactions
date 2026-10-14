import sys
from collections import defaultdict

totals = defaultdict(int)

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    key, value = line.split("\t", 1)

    if key != "TOTAL":
        continue

    category, amount = value.split(",", 1)
    amount_cents = int(round(float(amount) * 100))
    totals[category] += amount_cents

if totals:
    winner = max(totals, key=lambda category: totals[category])

    print("leader_category\t{}".format(winner))
    print("leader_total\t{:.2f}".format(totals[winner] / 100.0))

    for category, total_cents in sorted(
        totals.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        print("category_total\t{},{}".format(
            category, total_cents / 100.0
        ))
