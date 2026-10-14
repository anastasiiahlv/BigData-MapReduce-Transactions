import csv
import sys
from datetime import datetime

reader = csv.reader(sys.stdin)

for row in reader:
    if not row or row[0] == "user_id":
        continue

    try:
        user_id, timestamp, category, amount = row
        date = datetime.strptime(
            timestamp, "%Y-%m-%dT%H:%M:%S"
        ).strftime("%Y-%m-%d")

        amount_cents = int(round(float(amount) * 100))
        print("{}|{}\t{}".format(date, category, amount_cents))

    except (ValueError, TypeError):
        print("Некоректний рядок: {}".format(row), file=sys.stderr)
