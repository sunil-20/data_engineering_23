# Group_schedule table.
from random import seed
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator
from datetime import datetime, timedelta

class Group_schedule:
    def __init__(self, x):
        self.x = x
        self.f = Faker()
        self.uid_gen = UIDGenerator(self.f)
    


        #seed
        seed(2)

    # erdlab import
#     Group_schedule {
# 	group_schedule_id integer pk null increments
# 	number integer
# 	course_id integer > Course.course_id
# }