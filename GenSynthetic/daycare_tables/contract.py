# Contract table.
from random import seed
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator
from datetime import datetime, timedelta

class Contract:
    def __init__(self, x):
        self.x = x
        self.f = Faker()
        self.uid_gen = UIDGenerator(self.f)

        # set seed
        seed(2)

        # #define list for data generation
        self.contract_number = ["AAA","BBB","CCC","DDD"]

    # generate table
    def generate_data(self, digits_id=3):
        data = pd.DataFrame()
        for i in range(self.x):
            data.loc[i, "contract_id"] = i+1 # increment by 1
            data.loc[i, "consent_doc_number"] = self.f.random_element(elements=self.contract_number)
            today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
            start_date = self.f.date_between(start_date=today, end_date=today + timedelta(days=1000))
            data.loc[i, "start_date"] = start_date

            # generate stop date between start_date and the next 10 years
            stop_date = self.f.date_between(start_date=start_date, end_date=start_date + timedelta(days=365*3))
            data.loc[i, "end_date"] = stop_date

    # convert to datetime
        data["start_date"] = pd.to_datetime(data["start_date"])
        data["end_date"] = pd.to_datetime(data["end_date"])

        return data 
    
#erdlab import 
# Contract {
# 	contract_id integer pk increments
# 	number string
# 	start_date date
# 	end_date date null
# 	transaction_id integer > Transactions.transaction_id
# }
