# Staff table.
from random import seed
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator

class Staff:
    def __init__(self, x):
        self.x = x
        self.f = Faker()
        self.uid_gen = UIDGenerator(self.f)

        # set seed
        seed(2)

    # generate table
    def generate_data(self, digits_id=3):
        data = pd.DataFrame()
        for i in range(self.x):
            data.loc[i, "staff_id"] = self.uid_gen.generate_uid(digits_id)
            data.loc[i, "name"] = self.f.name()
            data.loc[i, "dob"] = self.f.date_of_birth(minimum_age=20, maximum_age=40)
            data.loc[i, "phone"] = self.f.phone_number() # odd phones generated need to create random list for consistency
            data.loc[i, "address"] = self.f.address()
            data.loc[i, "gender"] = self.f.random_element(elements=["Male", "Female", "Other"])
            data.loc[i, "caregiver_id"] = self.uid_gen.generate_uid(digits_id)
            data.loc[i, "transaction_id"] = self.uid_gen.generate_uid(digits_id)

        # convert to datetime
        data["dob"] = pd.to_datetime(data["dob"])

        return data


#erdlab
# Staff {
# 	staff_id integer pk increments
# 	name varchar
# 	dob date
# 	phone integer
# 	address varchar
# 	gender varchar
# 	caregiver_id integer null > Caregiver.caregiver_id
# 	transaction_id integer > Transactions.transaction_id
# }