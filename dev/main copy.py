# main.py
import os

# set the working directory to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

from uid_generator import UIDGenerator
from transactions import Transactions
from activity import Activity
from staff import Staff
from staff_salary import Staff_salary
from fee import Fee
from group import Group
from suppliers import Suppliers
from contract import Contract
from products import Products
from orders import Orders
from parent import Parent
from kid import Kid
from assessment import Assessment

# create a folder
export_to_folder = "csv_tables44"
export_to_path = os.path.join(script_dir, export_to_folder)

if not os.path.exists(export_to_path):
    os.makedirs(export_to_path)
    print(f"Export path: {export_to_path}")

# set seed
seed_value = 42
# Generate UIDGenerator instance

uid_gen = UIDGenerator(digit_count=6, seed=seed_value)

# 1. Generate Transactions Instance and data
transaction_instance = Transactions(x=182, uid_gen=uid_gen)
transaction_data = transaction_instance.generate_transaction_data()
transaction_data.to_csv(f"{export_to_path}/transaction.csv", index = False)
print("Transaction table created")

# 2. Create Activity Instance and data
activity_instance = Activity(x=40)
activity_data = activity_instance.generate_activity_data()
activity_data.to_csv(f"{export_to_path}/activity.csv", index = False)
print("Activity table created")

# 3. Generate Group instance and data
group_instance = Group(x=2)
group_data = group_instance.generate_group_data()
group_data.to_csv(f"{export_to_path}/daycare_group.csv", index=False)
print("Group table Created")

# 4. Generate Suppliers instance and data
suppliers_instance = Suppliers(x=15, uid_gen=uid_gen)
suppliers_data = suppliers_instance.generate_suppliers_data()
suppliers_data.to_csv(f"{export_to_path}/suppliers.csv", index=False)
print("Suppliers table created")

# 5. Generate Staff instance and data, pass staff_salary_instance
staff_instance = Staff(x=22, uid_gen=uid_gen, group_instance = group_instance)
staff_data = staff_instance.generate_staff_data()
staff_data.to_csv(f"{export_to_path}/staff.csv", index=False)
print("Staff table Created")

# 6. Generate Staff_salary Instance and data
staff_salary_instance = Staff_salary(x= 22, uid_gen=uid_gen, transaction_instance=transaction_instance, staff_instance= staff_instance, staff_data=staff_data)
staff_salary_data = staff_salary_instance.generate_staff_salary_data()
staff_salary_data.to_csv(f"{export_to_path}/staff_salary.csv", index = False)
print("Staff salary table created")

# 7. Generate Fee instance and data
fee_instance = Fee(x=100, uid_gen=uid_gen, transaction_instance=transaction_instance)
fee_data = fee_instance.generate_fee_data() # call method generate_data()
fee_data.to_csv(f"{export_to_path}/fee.csv", index = False)
print("Fee table Created")

# 8. Generate Contract instance and data
contract_instance = Contract(x=100, uid_gen=uid_gen)
contract_data = contract_instance.generate_contract_data()
contract_data.to_csv(f"{export_to_path}/contract.csv", index = False)
print("Contract table Created")

# 9. Generate Products instance and data
products_instance = Products(x=60, uid_gen=uid_gen, suppliers_instance=suppliers_instance)
products_data = products_instance.generate_products_data()
products_data.to_csv(f"{export_to_path}/products.csv", index=False)
print("Product table Created")

# 10. Generate Orders Instance and data
orders_instance = Orders(x=60, uid_gen=uid_gen, transaction_instance=transaction_instance, activity_instance= activity_instance, products_instance= products_instance)
orders_data = orders_instance.generate_orders_data()
orders_data.to_csv(f"{export_to_path}/orders.csv", index=False)
print("Orders table Created")

# 11. Generate Parent Instance and  data
parent_instance = Parent(x=100, uid_gen=uid_gen, contract_instance=contract_instance)
parent_data = parent_instance.generate_parent_data()
parent_data.to_csv(f"{export_to_path}/parent.csv", index=False)
print("Parent table Created")

# 12. Generate Kid instance and data, passing parent_instance, group_instance, and products_instance
kid_instance = Kid(x=100, uid_gen=uid_gen, parent_instance=parent_instance, group_instance=group_instance)
kid_data = kid_instance.generate_kid_data()
kid_data.to_csv(f"{export_to_path}/kid.csv", index=False)
print("Kid table Created")

# 13. Generate Assessment instance and data, passing kid_instance and activity_instance
assessment_instance = Assessment(x=100, uid_gen=uid_gen, kid_instance=kid_instance, activity_instance=activity_instance)
assessment_data = assessment_instance.generate_assessment_data()
assessment_data.to_csv(f"{export_to_path}/assessment.csv", index=False)
print("Assessment table Created")