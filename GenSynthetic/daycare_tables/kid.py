# Kid table.
from random import seed
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator
#from daycare_tables.uid_generator import UIDGenerator

class Kid:
    def __init__(self, x):
        self.x = x
        self.f = Faker()
        self.uid_gen = UIDGenerator(self.f)

        # set seed
        seed(2)

    # generate table
    def generate_data(self, digits_kid=3, digits_parent=3, digits_other=4):
        data = pd.DataFrame()
        for i in range(self.x):
            data.loc[i, "kid_id"] = self.uid_gen.generate_uid(digits_kid)
            data.loc[i, "name"] = self.f.name()
            data.loc[i, "dob"] = self.f.date_of_birth(minimum_age=0, maximum_age=5)
            data.loc[i, "parent_id"] = self.uid_gen.generate_uid(digits_parent)
            data.loc[i, "medical_id"] = self.uid_gen.generate_uid(digits_other)
            data.loc[i, "group_id"] = self.uid_gen.generate_uid(digits_other)

        # convert to datetime
        data["dob"] = pd.to_datetime(data["dob"])

        return data

# Data types and column names from erdlab

# Kid {
# 	kid_id integer > Kid_schedule.kid_id
# 	name varchar
# 	dob date
# 	parent_id integer > Parent.parent_id
# 	medical_id integer null > Medical_details.medical_id
# 	group_id integer > Group.group_id
# }


