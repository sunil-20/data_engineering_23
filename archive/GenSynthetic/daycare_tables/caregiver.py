# Caregiver table.
from random import seed
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator
from datetime import datetime, timedelta

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
    def generate_data(self, digits_id=3):
        data = pd.DataFrame()
        for i in range(self.x):
            data.loc[i, "caregiver_id"] = self.uid_gen.generate_uid(digits_id)
            data.loc[i, "caregiver_name"] = self.f.name()
            data.loc[i, "certificate_type"] = self.f.random_element(elements=self.certificte_type)
            today = datetime.today()
            future_date = today.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=self.f.random_int(min=1, max=3650)) 
            data.loc[i, "certificate_expiration_date"]= future_date
        # convert to datetime
        data["certificate_expiration_date"] = pd.to_datetime(data["certificate_expiration_date"])

        return data
    
    #erdlab import 
    # caregiver_id integer pk null increments
	# certificate_type varchar
	# certificate_expiration_date date