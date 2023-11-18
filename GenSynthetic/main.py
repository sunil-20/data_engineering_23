import pandas as pd
import os
from daycare_tables import (
    Kid, Caregiver, Consent, Contract, Course,
    Group_schedule, Group, Kid_schedule, Medical_details,
    Orders_details, Orders, Parent, Products, Staff,
    Stocks, Suppliers, Transactions, Medication_log
)

# set the working directory to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# create a folder
export_to_folder = "csv_tables"
if not os.path.exists(export_to_folder):
    os.makedirs(export_to_folder)

# Define a list of tuples with table class and x value
tables = [
    (Kid, 100),
    (Caregiver, 20),
    (Consent, 20),
    (Contract, 20),
    (Course, 100),
    (Group_schedule, 100),
    (Group, 100),
    (Kid_schedule, 100),
    (Medical_details, 100),
    (Orders_details, 100),
    (Orders, 100),
    (Parent, 100),
    (Products, 100),
    (Staff, 20),
    (Stocks, 100),
    (Suppliers, 10),
    (Transactions, 100),
    (Medication_log, 40)
]

# Loop through the tables and generate/export data
for table_class, x_value in tables:
    instance = table_class(x=x_value)
    table_data = instance.generate_data()
    table_name = table_class.__name__.lower()
    table_data.to_csv(f"{export_to_folder}/{table_name}.csv", index=False)
