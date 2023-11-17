# main table.
import pandas as pd
from daycare_tables.kid import Kid

# generate kid table
kid_instance = Kid(x=100)
kid_data = kid_instance.generate_data()

#save_to_CSV
kid_data.to_csv("kid.csv", index = False)