# main table.
import pandas as pd
from daycare_tables.kid import Kid
from daycare_tables.caregiver import Caregiver
from daycare_tables.consent import Consent
from daycare_tables.contract import Contract
from daycare_tables.course import Course

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