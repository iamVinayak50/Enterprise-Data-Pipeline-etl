import pandas as pd
import numpy as np
import random
import string
import os
from faker import Faker

fake = Faker()

def messy_string():
    return ''.join(random.choice(string.ascii_letters + string.digits + "   ,,;;--") for _ in range(random.randint(5,20)))

def gen_sap_cars(n):
    models=["Range Rover Sport","Defender 110","Discovery","Evoque","Velar"]
    variants=["SE","HSE","Dynamic","S","R-Dynamic"]
    engines=["Petrol","Diesel","Hybrid","Electric"]
    plants=["Solihull","Nitra","Halewood"]
    data=[]
    for i in range(n):
        data.append([
            f"JLR{1000+i}",
            random.choice(models),
            random.choice(variants),
            random.choice(engines),
            random.choice(plants),
            fake.date_between(start_date="-2y", end_date="today"),
        ])
    return pd.DataFrame(data, columns=["CAR_ID","MODEL","VARIANT","ENGINE_TYPE","PLANT","MANUFACTURE_DATE"])

def gen_sap_parts(n):
    suppliers=["Bosch","Denso","Valeo","ZF","Magna"]
    data=[]
    for i in range(n):
        data.append([
            f"PRT{1000+i}",
            messy_string(),
            f"JLR{1000+random.randint(0,99999)}",
            random.choice(suppliers),
            round(random.uniform(20,500),2),
            fake.date_between(start_date="-1y", end_date="today"),
        ])
    return pd.DataFrame(data, columns=["PART_ID","PART_NAME","CAR_ID","SUPPLIER","COST","UPDATED_DATE"])

def gen_vista_sales(n):
    data=[]
    for i in range(n):
        data.append([
            f"SL{1000+i}",
            f"JLR{1000+random.randint(0,99999)}",
            f"DL{random.randint(1,500)}",
            fake.date_between(start_date="-1y", end_date="today"),
            round(random.uniform(30000,150000),2),
            fake.name(),
        ])
    return pd.DataFrame(data, columns=["SALE_ID","CAR_ID","DEALER_ID","SALE_DATE","PRICE","CUSTOMER_NAME"])

def gen_vista_dealers(n):
    data=[]
    for i in range(n):
        data.append([
            f"DL{i+1}",
            fake.company(),
            fake.country(),
            fake.city(),
            fake.phone_number(),
        ])
    return pd.DataFrame(data, columns=["DEALER_ID","DEALER_NAME","COUNTRY","CITY","CONTACT"])

def gen_iqm_service(n):
    service_types=["Maintenance","Repair","Warranty","Inspection"]
    centers=["Solihull Workshop","Mumbai Workshop","London Workshop","Pune Workshop"]
    data=[]
    for i in range(n):
        data.append([
            f"SRV{1000+i}",
            f"JLR{1000+random.randint(0,99999)}",
            random.choice(service_types),
            random.choice(centers),
            fake.date_between(start_date="-1y", end_date="today"),
            round(random.uniform(0,3000),2),
        ])
    return pd.DataFrame(data, columns=["SERVICE_ID","CAR_ID","SERVICE_TYPE","SERVICE_CENTER","SERVICE_DATE","COST"])

# generate data
N = 100000

dfs = {
    "sap_cars_raw.csv": gen_sap_cars(N),
    "sap_parts_raw.csv": gen_sap_parts(N),
    "vista_sales_raw.csv": gen_vista_sales(N),
    "vista_dealers_raw.csv": gen_vista_dealers(500),  # FIX
    "iqm_service_raw.csv": gen_iqm_service(N),
}

for filename, df in dfs.items():
    df.to_csv(f"data/{filename}", index=False)

list(os.listdir("data"))
