# Kid_schedule table.
from random import seed, randint
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator

class Kid_schedule:
    def __init__(self, x):
        self.x = x
        self.f = Faker()
        self.uid_gen = UIDGenerator(self.f)

        # set seed
        seed(2)

        # #define list for data generation
        self.need_meal = ["Y", "N"]
        self.day_type = [ "type1", "type2", "type3"]

    # generate table
    def generate_data(self):
        data = pd.DataFrame()
        for i in range(self.x):
            data.loc[i, "kid_id"] = i+1 # increment by 1
            data.loc[i, "day_week"] = randint(1,5)
            data.loc[i, "day_type"] = self.f.random_element(elements=self.day_type)
            data.loc[i, "need_meal"] = self.f.random_element(elements=self.need_meal)
        return data 
    


#erdlab import
# Kid_schedule {
# 	kid_id integer pk increments
# 	day_of_week varchar > Day_of_week.day_of_week_id
# 	day_type varchar > Half_day.half_day_id
# 	need_meal boolean
# }