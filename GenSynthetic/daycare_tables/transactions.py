# Transactions table.
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator
from datetime import datetime, timedelta
from random import seed

class Transactions:
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
            data.loc[i, "transaction_id"] = self.uid_gen.generate_uid(digits_id)
            data.loc[i, "card_number"] = self.f.credit_card_number(card_type=None)
            data.loc[i, "total"] = self.f.random_int(min=10, max=1000)
            data.loc[i, "amount"] = self.f.random_int(min=1, max=data.loc[i, "total"])
            data.loc[i, "due_date"] = self.f.date_between_dates(
                date_start=datetime.now(),
                date_end=datetime.now() + timedelta(days=365)
            )
            data.loc[i, "date"] = self.f.date_this_decade()
            data.loc[i, "name"] = self.f.name()
            data.loc[i, "type"] = self.f.random_element(elements=["Credit", "Debit", "Check"])

        return data



#erdlab
# Transactions {
# 	transaction_id integer pk increments
# 	card_number varchar null
# 	total integer
# 	amount integer
# 	due_date date null
# 	date date
# 	name varchar
# 	type varchar
# }


