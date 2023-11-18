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