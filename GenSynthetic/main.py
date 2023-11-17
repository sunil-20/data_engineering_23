# main table.
import pandas as pd
from daycare_tables.kid import Kid
from daycare_tables.caregiver import Caregiver

# generate kid table
kid_instance = Kid(x=100)
kid_data = kid_instance.generate_data()
#save_to_CSV
kid_data.to_csv("kid.csv", index = False)


#generate caregiver table
caregiver_instance = Caregiver(x=20)
caregiver_data = caregiver_instance.generate_data()
#save to CSV
caregiver_data.to_csv("caregiver.csv", index = False)