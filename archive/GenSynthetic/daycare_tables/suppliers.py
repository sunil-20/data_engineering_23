# Suppliers table.
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator
from random import seed

class Suppliers:
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
            data.loc[i, "suppliers_id"] = self.uid_gen.generate_uid(digits_id)
            data.loc[i, "name"] = self.f.company()
            data.loc[i, "address"] = self.f.address()
            data.loc[i, "phone"] = self.f.phone_number()
            data.loc[i, "email"] = self.f.email()

        return data


#erdlab
# Suppliers {
# 	suppliers_id integer pk increments
# 	name varchar
# 	address varchar null
# 	phone varchar null
# 	email varchar null
# }
