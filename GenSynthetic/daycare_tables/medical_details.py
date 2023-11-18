# Medical_details table.
from random import seed
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator

class Medical_details:
    def __init__(self, x):
        self.x = x
        self.f = Faker()
        self.uid_gen = UIDGenerator(self.f)

        # set seed
        seed(2)

        # #define list for data generation
        self.food_allergy = ["AAA","BBB","CCC","DDD"]
        self.medic = ["Immunization", "Medication", "Dev milestone", "IEP program"]
        self.blood_group = ["A", "B", "AB", "O+", "O-"]
        self.neuro_type = ["ASD", "ADHD", "OCD","PTSD" "dyslexic","dyspraxia", "anxiety","depression"]

    # generate table
    def generate_data(self, digits_id=3):
        data = pd.DataFrame()
        for i in range(self.x):
            data.loc[i, "medical_id"] = i+1 # increment by 1
            data.loc[i, "food_allergy"] = self.f.random_element(elements=self.food_allergy)
            data.loc[i, "medication"] = self.f.random_element(elements=self.medic)
            data.loc[i, "emergency_phone"] = self.f.phone_number()
            data.loc[i, "blood_group"] = self.f.random_element(elements=self.blood_group)
            data.loc[i, "neurotype"] = self.f.random_element(elements=self.neuro_type)



        return data 
    
    #erdlab
#     Medical_details {
# 	medical_id integer pk increments
# 	food_allergy varchar
# 	medication varchar
# 	emergency_phone varchar
# 	blood_group varchar
# 	neurotype varchar
# }