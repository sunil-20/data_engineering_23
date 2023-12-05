# Course table.
from random import seed, randint
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator
from datetime import datetime, timedelta

class Course:
    def __init__(self, x):
        self.x = x
        self.f = Faker()
        self.uid_gen = UIDGenerator(self.f)

        # set seed
        seed(2)

        # #define list for data generation
        self.course_ = ["AAA","BBB","CCC","DDD"]
        self.day_type = [ "type1", "type2", "type3"]

    # generate table
    def generate_data(self, uid_int=3):
        data = pd.DataFrame()
        for i in range(self.x):
            data.loc[i, "course_id"] = i+1 # increment by 1
            data.loc[i, "course_name"] = self.f.random_element(elements=self.course_)
            data.loc[i, "duration"] = self.uid_gen.generate_uid(uid_int)
            data.loc[i, "order_id"] = self.uid_gen.generate_uid(uid_int)
            data.loc[i, "day_week"] = randint(1,5)
            data.loc[i, "day_type"] = self.f.random_element(elements = self.day_type)

        return data 
    

# erdlab import

# Course {
# 	course_id decimal pk null increments
# 	name integer
# 	duration integer null
# 	orders_id integer > Orders.orders_id
# 	day_week varchar
# 	day_type varchar
# }
