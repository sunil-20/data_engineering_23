# Caregiver table.
from random import seed
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator


class Caregiver:
    def __init__(self, x):
        self.x = x
        self.f = Faker()
        self.uid_gen = UIDGenerator(self.f)

        # set seed
        seed(2)

        #define list for data generation
        self.certificte_type = ["A","B","C","D"]

    # generate table
    def generate_data(self, digits_id=3, digits_parent=3, digits_other=4):
        data = pd.DataFrame()
        for i in range(self.x):
            data.loc[i, "caregiver_id"] = self.uid_gen.generate_uid(digits_id)
            data.loc[i, "caregiver_name"] = self.f.name()
            data.loc[i, "certificate_type"] = self.f.random_element(elements=self.certificte_type)
            data.loc[i, "certificate_expiration_date"]= self.f.date_future(end_date='+10y', tzinfo=None)
            
        # convert to datetime
        data["certification_expiration_date"] = pd.to_datetime(data["certification_expiration_date"])

        return data
    
    #erdlab import 
    # caregiver_id integer pk null increments
	# certificate_type varchar
	# certificate_expiration_date date