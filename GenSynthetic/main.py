# main table.
import pandas as pd

from daycare_tables.kid import Kid
from daycare_tables.caregiver import Caregiver
from daycare_tables.consent import Consent
from daycare_tables.contract import Contract
from daycare_tables.course import Course
from daycare_tables.group_schedule import Group_schedule
from daycare_tables.group import Group
from daycare_tables.kid_schedule import Kid_schedule
from daycare_tables.medical_details import Medical_details
from daycare_tables.orders_details import Orders_details
from daycare_tables.orders import Orders
from daycare_tables.parent import Parent
from daycare_tables.products import Products
from daycare_tables.staff import Staff
from daycare_tables.stocks import Stocks
from daycare_tables.suppliers import Suppliers
from daycare_tables.transactions import Transactions
#generate kid table
kid_instance = Kid(x=100)
kid_data = kid_instance.generate_data()
#save_to_CSV
kid_data.to_csv("csv_tables/kid.csv", index = False)

#generate caregiver table
caregiver_instance = Caregiver(x=20)
caregiver_data = caregiver_instance.generate_data()
#save to CSV
caregiver_data.to_csv("csv_tables/caregiver.csv", index = False)

#generate consent table
consent_instance = Consent(x=20)
consent_data = consent_instance.generate_data()
#save to CSV
consent_data.to_csv("csv_tables/consent.csv", index = False)

#generate contract table
contract_instance = Contract(x=20)
contract_data = contract_instance.generate_data()
#save
contract_data.to_csv("csv_tables/contract.csv", index = False)

#generate course table
course_instance = Course(x=100)
course_data = course_instance.generate_data()
#save
course_data.to_csv("csv_tables/course.csv", index = False)

#generate group_schedule table
group_schedule_instance = Group_schedule(x=100)
group_schedule_data = group_schedule_instance.generate_data()
#save
group_schedule_data.to_csv("csv_tables/group_schedule.csv", index = False)

#generate group
group_instance = Group(x = 100)
group_data = group_instance.generate_data()
#save
group_data.to_csv("csv_tables/group.csv", index = False)

#generate kid_schedule
kid_schedule_instance = Kid_schedule(x = 100)
kid_schedule_data = kid_schedule_instance.generate_data()
#save
kid_schedule_data.to_csv("csv_tables/kid_schedule.csv", index = False)

#generate medical_details 
medical_details_instance = Medical_details(x = 100)
medical_data = medical_details_instance.generate_data()
#save
medical_data.to_csv("csv_tables/medical_details.csv", index = False)

# generate orders_details table
orders_details_instance = Orders_details(x=100)
orders_details_data = orders_details_instance.generate_data()
# save to CSV
orders_details_data.to_csv("csv_tables/orders_details.csv", index=False)

# generate orders table
orders_instance = Orders(x=100)
orders_data = orders_instance.generate_data()
# save to CSV
orders_data.to_csv("csv_tables/orders.csv", index=False)

# generate parent table
parent_instance = Parent(x=100)
parent_data = parent_instance.generate_data()
# save to CSV
parent_data.to_csv("csv_tables/parent.csv", index=False)

# generate products table
products_instance = Products(x=100)
products_data = products_instance.generate_data()
# save to CSV
products_data.to_csv("csv_tables/products.csv", index=False)

# generate staff table
staff_instance = Staff(x=20)
staff_data = staff_instance.generate_data()
# save to CSV
staff_data.to_csv("csv_tables/staff.csv", index=False)

# generate stocks table
stocks_instance = Stocks(x=100)
stocks_data = stocks_instance.generate_data()
# save to CSV
stocks_data.to_csv("csv_tables/stocks.csv", index=False)

# generate suppliers table
suppliers_instance = Suppliers(x=10)
suppliers_data = suppliers_instance.generate_data()
# save to CSV
suppliers_data.to_csv("csv_tables/suppliers.csv", index=False)

# generate transactions table
transactions_instance = Transactions(x=100)
transactions_data = transactions_instance.generate_data()
# save to CSV
transactions_data.to_csv("csv_tables/transactions.csv", index=False)