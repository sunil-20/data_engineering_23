# medication_log.py
from random import seed, randint
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator

class Medication_log:
    def __init__(self, x):
        self.x = x
        self.f = Faker()
        self.uid_gen = UIDGenerator(self.f)

        # set seed
        seed(2)

        # define list for data generation
        self.health_problems = ["Flu", "Asthma", "Hay fever", "Eczema", "Constipation"]
        self.administration_routes = ["Oral", "Inhaled", "Cutaneous", "EpiPen", "Injection"]
        self.medication_names = ["Paracetamol", "Ciclesonide", "Antihistamine", "Emollients & Moisturiser", "Docusate", "Fluticasone"]


    # generate table
    def generate_data(self):
        data = pd.DataFrame()
        for i in range(self.x):
            data.loc[i, "medical_id"] = self.uid_gen.generate_uid(3)
            data.loc[i, "health_problem"] = self.f.random_element(elements=self.health_problems)
            data.loc[i, "medication_id"] = self.uid_gen.generate_uid(3)
            data.loc[i, "medication_name"] = self.f.random_element(elements=self.medication_names)
            data.loc[i, "administration_route"] = self.f.random_element(elements=self.administration_routes)
            data.loc[i, "dose (ml/g)"] = self.f.random_element(elements=["2.5ml", "0.5mg", "30g", "12.5mg"])
            data.loc[i, "qty_day"] = 1 
            data.loc[i, "date"] = self.f.date_this_decade()
            data.loc[i, "time"] = self.f.time_object().strftime("%H:%M:%S")
            data.loc[i, "staff_id"] = self.uid_gen.generate_uid(2)

        # convert date to datetime
        data["date"] = pd.to_datetime(data["date"])

        return data
