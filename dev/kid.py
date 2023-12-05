# Kid table.
import pandas as pd
import random

class Kid:
    """
    A class representing kids with associated details.

    Parameters:
    - x (int): The number of kids to generate.
    - uid_gen (object): An instance of a UID generator for creating unique IDs.
    - parent_instance (object): An instance of the Parent class to fetch parent IDs.
    - group_instance (object): An instance of the Group class to fetch group IDs.

    Attributes:
    - x (int): The number of kids to generate.
    - uid_gen (object): An instance of a UID generator for creating unique IDs.
    - parent_instance (object): An instance of the Parent class to fetch parent IDs.
    - group_instance (object): An instance of the Group class to fetch group IDs.
    - kid_ids (list): A list containing unique kid IDs generated for the kids.
    - kid_data (DataFrame): A pandas DataFrame containing information about the generated kids.

    Methods:
    - generate_kid_ids(): Generates a list of unique kid IDs starting from 200 and ending at 200 + x.
    - generate_kid_data(): Generates a pandas DataFrame with details of the kids, including ID, name, date of birth, parent ID, group ID, food type, and schedule.

    Usage:
    kid_instance = Kid(x=100, uid_gen=my_uid_generator, parent_instance=my_parents, group_instance=my_groups)
    generated_kid_ids = kid_instance.kid_ids
    generated_kid_data = kid_instance.kid_data
    """
    def __init__(self, x, uid_gen, parent_instance, group_instance):
        self.x = x
        self.uid_gen = uid_gen
        # To fetch parent ids
        self.parent_instance = parent_instance
        # To fetch group ids
        self.group_instance = group_instance

        self.kid_ids = self.generate_kid_ids()
        self.kid_data = self.generate_kid_data()
    
    # Make a list starting from 200 and ending at 200+x value
    def generate_kid_ids(self): 
        return list(range(200, 200+self.x))
    
    def generate_kid_data(self):
        data = pd.DataFrame()

        parent_ids = self.parent_instance.parent_ids
        random.shuffle(parent_ids)
        
        kid_ids = self.kid_ids.copy()
        random.shuffle(kid_ids)
        
        group_ids = self.group_instance.group_ids

        for i, parent_id in enumerate(parent_ids):
            data.loc[i, "kid_id"] = self.kid_ids[i]
            data.loc[i, "kid_name"] = self.uid_gen.f.name()
            data.loc[i, "dob"] = self.uid_gen.f.date_of_birth()

            # Link to Parent table 
            data.loc[i, "parent_id"] = parent_id

            # Link to Group table
            data.loc[i, "group_id"] = random.choice(group_ids)

            data.loc[i, "food_type"] = self.uid_gen.f.random_element(["food-normal", "food-allergy"])

            data.loc[i, "schedule"] = self.uid_gen.f.random_element(["full time", "part time"])

        return data


# Data types and column names from erdlab

# Kid {
# 	kid_id integer > Kid_schedule.kid_id
# 	name varchar
# 	dob date
# 	parent_id integer > Parent.parent_id
# 	medical_id integer null > Medical_details.medical_id
# 	group_id integer > Group.group_id
# }

# kid_id: 1,2,3,4,5, ...
# kid_name : "Joe Doe", "Jane Doe", ...
# dob: "2020-01-19,", ...
# parent_id: 34, 56, 78, ...
# group_id: 123,123,123, ...
# food_type: "food-normal", "food-allergy" (2 categories)
# product_id: 123,12, 13, ...
# schedule: "full time", "part time" (2 categories)
