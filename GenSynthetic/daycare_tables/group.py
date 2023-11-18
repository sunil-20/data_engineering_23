# Group table.
from random import seed, randint
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator

class Group:
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
            data.loc[i, "group_id"] = i+1 # increment by 1
            data.loc[i, "start_age"] = randint(0, 5)
            data.loc[i, "end_age"] = randint(4, 5)
            data.loc[i, "caregiver_id"] = self.uid_gen.generate_uid(digits_id)
            data.loc[i, "group_schedule_id"] = self.uid_gen.generate_uid(digits_id)

        return data 

# erdlab import 
# Group {
# 	group_id integer pk null increments
# 	start_age date null
# 	end_age date null
# 	caregiver_id integer > Caregiver.caregiver_id
# 	group_schedule_id integer > Group_schedule.group_schedule_id
# }