import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

SEED = 20261014
NUM_TRANSACTIONS = 600_000

OUTPUT_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "transactions.csv"
)

CATEGORIES = [
    "groceries",
    "electronics",
    "books",
    "clothing",
    "health",
    "home",
    "sports",
    "beauty",
]


CATEGORY_WEIGHTS = [30, 12, 10, 14, 9, 10, 8, 7]

def main():
    random.seed(SEED)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    start_date = datetime(2026, 1, 1)
    number_of_days = 90

    with OUTPUT_FILE.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file, lineterminator="\n")

        writer.writerow([
            "user_id",
            "timestamp",
            "category",
            "amount",
        ])

        for _ in range(NUM_TRANSACTIONS):
            day_offset = random.randrange(number_of_days)
            seconds = random.randrange(24 * 60 * 60)

            timestamp = (
                start_date
                + timedelta(days=day_offset, seconds=seconds)
            )

            category = random.choices(
                CATEGORIES,
                weights=CATEGORY_WEIGHTS,
                k=1,
            )[0]

            user_id = random.randint(1000, 9999)

            amount_cents = random.randint(100, 150000)
            amount = f"{amount_cents / 100:.2f}"

            writer.writerow([
                user_id,
                timestamp.strftime("%Y-%m-%dT%H:%M:%S"),
                category,
                amount,
            ])

    print(f"Файл створено: {OUTPUT_FILE}")
    print(f"Кількість транзакцій: {NUM_TRANSACTIONS:,}")
    print(f"Розмір файлу: {OUTPUT_FILE.stat().st_size / 1024**2:.2f} MiB")


if __name__ == "__main__":
    main()
