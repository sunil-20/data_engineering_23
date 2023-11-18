# Group_schedule table.
from random import seed, randint
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator


class Group_schedule:
    def __init__(self, x):
        self.x = x
        self.f = Faker()
        self.uid_gen = UIDGenerator(self.f)
    
        #seed
        seed(2)
    def generate_data(self, digits_id = 3):
        data = pd.DataFrame()
        for i in range(self.x):
            data.loc[i,"group_schedule_id"] = self.uid_gen.generate_uid(digits_id)
            data.loc[i, "number"] = randint(1, 100)
            data.loc[i, "course_id"] = randint(2, 10)
        return data
    

    # erdlab import
#     Group_schedule {
# 	group_schedule_id integer pk null increments
# 	number integer
# 	course_id integer > Course.course_id
# }