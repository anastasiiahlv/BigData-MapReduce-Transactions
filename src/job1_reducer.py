import sys

current_key = None
current_total = 0


def emit(key, total_cents):
    if key is None:
        return

    date, category = key.split("|", 1)
    total = total_cents / 100.0

    print("{}\t{:.2f}".format(
        "{},{}".format(date, category), total
    ))


for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    key, value = line.split("\t", 1)
    amount_cents = int(value)

    if key == current_key:
        current_total += amount_cents
    else:
        emit(current_key, current_total)
        current_key = key
        current_total = amount_cents

emit(current_key, current_total)
