import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        daily_key, total = line.split("\t", 1)
        date, category = daily_key.split(",", 1)

        print("TOTAL\t{},{}".format(category, total))

    except ValueError:
        print("Некоректний рядок Job 1: {}".format(line),
              file=sys.stderr)
