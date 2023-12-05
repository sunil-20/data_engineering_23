import pandas as pd
import random

class Group:
    """
    A class representing groups of children in an educational setting.

    Parameters:
        x (int): The number of groups to generate.

    Attributes:
        x (int): The number of groups to generate.
        group_info (dict): A dictionary mapping group names to their corresponding group IDs.
        age_group (dict): A dictionary mapping group names to their corresponding age groups.
        group_ids (list): A list of unique group IDs.
        group_data (pd.DataFrame): A DataFrame containing group details.

    Methods:
        generate_group_ids(): Generates a list of unique group IDs based on group names.
        generate_group_data(): Generates group data with group IDs, names, and associated age groups.
    """
    def __init__(self, x):
        self.x = x
        self.group_info = {"Honey Bee": 1012, "Tiny Tiger": 1034}
        self.age_group = { "Honey Bee": "1-2","Tiny Tiger": "3-4"}
        self.group_ids = self.generate_group_ids()
        self.group_data=self.generate_group_data()
    
    def generate_group_ids(self):
        return[self.group_info[name] for name in self.group_info]

    def generate_group_data(self):
        data = pd.DataFrame()
        group_ids = list(self.group_info.values())[:self.x]

        # pick groups
        unique_group_names = random.sample(list(self.group_info.keys()), 2)
        for i in range(self.x):
            data.loc[i,"group_id"] = group_ids[i]
            data.loc[i, "group_name"] = unique_group_names[i % 2]
            data.loc[i, "group_age"] = self.age_group[data.loc[i, "group_name"]]
        return data


# erdlab import 
# Group {
# 	group_id integer pk increments
# 	group_age varchar increments unique
# 	staff_id integer > Staff.staff_id 1:m
# 	course_id integer > Course.course_id 1:m
# }
