# Orders table.
from random import seed
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator

class Orders:
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
            data.loc[i, "orders_id"] = self.uid_gen.generate_uid(digits_id)
            data.loc[i, "invoice"] = self.f.uuid4()  
            data.loc[i, "transaction_id"] = self.uid_gen.generate_uid(digits_id) 
            data.loc[i, "card_number"] = self.f.credit_card_number(card_type="mastercard") 
            data.loc[i, "total"] = self.f.random_int(min=100, max=1000)  
            data.loc[i, "pay"] = self.f.random_int(min=50, max=data.loc[i, "total"])  
            data.loc[i, "due_date"] = self.f.date_this_year()  
            data.loc[i, "date"] = self.f.date_between(start_date=data.loc[i, "due_date"]).strftime('%Y-%m-%d')

        return data

#erdlab
# Orders {
# 	orders_id integer pk increments
# 	invoice varchar null
# 	transaction_id integer > Transactions.transaction_id
# 	card_number varchar null
# 	total integer
# 	pay integer
# 	due_date date null
# 	date date
# }