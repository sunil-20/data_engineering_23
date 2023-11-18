import os

# Name of tables to be generated imported from erdlab
table_names = [
    "main",
    "Contract",
    "Group_schedule",
    "Caregiver",
    "Course",
    "Group",
    "Parent",
    "Kid",
    "Consent",
    "Staff",
    "Medical_details",
    "Kid_schedule",
    "Stocks",
    "Products",
    "Orders_details",
    "Suppliers",
    "Orders",
    "Transactions",
    "Medication_log"
]

# Create a separate directory/folder to save py files
directory = "daycare_tables"
os.makedirs(directory, exist_ok=True)

# Generate class files
for tbl in table_names:
    file_content = f"# {tbl} table."

    path_to_file = os.path.join(directory, f"{tbl.lower()}.py")

    with open(path_to_file, "w") as file:
        file.write(file_content)

    print(f"Created {tbl.lower()}.py")

print("Gen successful.")
