# Parent table.
from random import seed
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator

class Parent:
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
            data.loc[i, "parent_id"] = self.uid_gen.generate_uid(digits_id)
            data.loc[i, "name"] = self.f.name()
            data.loc[i, "phone"] = self.f.phone_number()
            data.loc[i, "address"] = self.f.address()
            data.loc[i, "email"] = self.f.email()
            data.loc[i, "consent_id"] = self.uid_gen.generate_uid(digits_id)  
            data.loc[i, "contract_id"] = self.uid_gen.generate_uid(digits_id)  

        return data


#erdlab
# Parent {
# 	parent_id integer pk increments
# 	name varchar
# 	phone varchar
# 	address varchar
# 	email varchar null
# 	consent_id integer > Consent.consent_id
# 	contract_id integer > Contract.contract_id
# }