# Stocks table.
from random import seed, randint, choice
import pandas as pd
from .uid_generator import UIDGenerator
from faker import Faker

class Stocks:
    def __init__(self, x):
        self.x = x
        self.f = Faker()
        self.uid_gen = UIDGenerator(self.f)
        
        # set seed
        seed(2)

    def generate_data(self, digits_id=3):
        data = pd.DataFrame()
        locations = ["A", "B", "C"]  # Example locations as placeholders need to change later

        for i in range(self.x):
            data.loc[i, "stocks_id"] = self.uid_gen.generate_uid(digits_id)
            data.loc[i, "products_id"] = self.uid_gen.generate_uid(digits_id)
            data.loc[i, "location"] = choice(locations)
            data.loc[i, "stock"] = randint(1, 100)

        return data

#erdlab
# Stocks {
# 	stocks_id integer pk increments
# 	products_id integer > Products.products_id
# 	location integer > users.id
# 	stock integer
# }