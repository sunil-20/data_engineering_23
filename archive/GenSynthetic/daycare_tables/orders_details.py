# Orders_details table.
from random import seed
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator

class Orders_details:
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
            data.loc[i, "orders_details_id"] = self.uid_gen.generate_uid(digits_id)
            data.loc[i, "orders_id"] = self.uid_gen.generate_uid(digits_id)  
            data.loc[i, "products_id"] = self.uid_gen.generate_uid(digits_id)  
            data.loc[i, "qty"] = self.f.random_int(min=1, max=10)  
            data.loc[i, "price"] = self.f.random_int(min=10, max=100)  
            data.loc[i, "total"] = data.loc[i, "qty"] * data.loc[i, "price"]  



        return data 
    
    #erdlab
#     Orders_details {
# 	orders_details_id integer pk increments
# 	orders_id integer > Orders.orders_id
# 	products_id integer > Products.products_id
# 	qty integer
# 	price integer
# 	total integer
# }