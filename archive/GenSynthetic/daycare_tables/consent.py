# Consent table.
from random import seed
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator
from datetime import datetime, timedelta

class Consent:
    def __init__(self, x):
        self.x = x
        self.f = Faker()
        self.uid_gen = UIDGenerator(self.f)

        # set seed
        seed(2)

        # #define list for data generation
        self.consent_number = ["AA","BB","CC","DD"]

    # generate table
    def generate_data(self, digits_id=3):
        data = pd.DataFrame()
        for i in range(self.x):
            data.loc[i, "consent_id"] = self.uid_gen.generate_uid(digits_id)
            #data.loc[i, "_name"] = self.f.name()
            data.loc[i, "consent_doc_number"] = self.f.random_element(elements=self.consent_number)
            today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
            start_date = self.f.date_between(start_date=today, end_date=today + timedelta(days=1000))
            data.loc[i, "start_date"] = start_date

            # generate stop date between start_date and the next 10 years
            stop_date = self.f.date_between(start_date=start_date, end_date=start_date + timedelta(days=365*3))
            data.loc[i, "stop_date"] = stop_date

    # convert to datetime
        data["start_date"] = pd.to_datetime(data["start_date"])
        data["stop_date"] = pd.to_datetime(data["stop_date"])

        return data 


# erdlab import

# Consent {
# 	consent_id integer pk null increments
# 	number varchar null
# 	start_date date null
# 	stop_date date
# }