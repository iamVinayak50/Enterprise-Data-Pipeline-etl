import csv
import random
from datetime import datetime, timedelta
import os

# ---------- SETTINGS ----------
NUM_RECORDS = 1000
OUTPUT_FOLDER = "data"
TODAY = datetime.now().strftime("%Y-%m-%d")
OUTPUT_FILE = f"{OUTPUT_FOLDER}/jlr_service_data_{TODAY}.csv"

# ---------- DATA LOOKUPS ----------
models = ["Defender", "Discovery", "Range Rover", "Range Rover Evoque", "Jaguar XF", "Jaguar F-Pace"]
regions = ["UK", "India", "USA", "Germany", "China", "Australia"]
issue_types = ["Oil Change", "Brake Pads", "Battery", "Engine", "Suspension", "Transmission"]
names = ["John Smith", "Rahul Mehta", "Alice Wong", "David Brown", "Sara Khan", "Peter White"]

# ---------- MAIN ----------
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["service_id", "vehicle_id", "model", "customer_name",
                     "service_date", "issue_type", "service_cost", "region", "feedback_score"])

    for i in range(NUM_RECORDS):
        service_id = f"S{1000 + i}"
        vehicle_id = f"V{3000 + i}"
        model = random.choice(models)
        customer = random.choice(names)
        service_date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
        issue = random.choice(issue_types)
        cost = random.randint(100, 1500)
        region = random.choice(regions)
        feedback = random.randint(1, 5)

        writer.writerow([service_id, vehicle_id, model, customer,
                         service_date, issue, cost, region, feedback])

print(f"✅ Generated file: {OUTPUT_FILE}")
