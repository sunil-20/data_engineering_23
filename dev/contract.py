# contract.py
import pandas as pd
import numpy as np
import string

class Contract:
    """
    A class representing contracts with associated details.

    Parameters:
    - x (int): The number of contracts to generate.
    - uid_gen (object): An instance of a UID generator for creating unique IDs.

    Attributes:
    - x (int): The number of contracts to generate.
    - uid_gen (object): An instance of a UID generator for creating unique IDs.
    - contract_ids (list): A list containing unique contract IDs generated for the contracts.
    - contract_data (DataFrame): A pandas DataFrame containing information about the generated contracts.

    Methods:
    - generate_contract_ids(): Generates a list of unique contract IDs based on the provided UID generator.
    - generate_contract_types(): Generates a list of contract types, ensuring a specified ratio of full-time and part-time contracts.
    - generate_contract_data(): Generates a pandas DataFrame with details of the contracts, including ID, document numbers, start and end dates, and contract type.

    Usage:
    contract_instance = Contract(x=10, uid_gen=my_uid_generator)
    generated_contract_ids = contract_instance.contract_ids
    generated_contract_data = contract_instance.contract_data
    """
    def __init__(self, x, uid_gen):
        self.x = x
        self.uid_gen = uid_gen
        self.contract_ids = self.generate_contract_ids()
        self.contract_data = self.generate_contract_data()

    def generate_contract_ids(self):
        return[self.uid_gen.generate_uid() for _ in range(self.x)]
    
    # generating contract types
    def generate_contract_types(self):
        num_full_time = 57
        num_part_time = 43

        contract_types = []
        while len(contract_types) < self.x:
            if len(contract_types) < num_full_time:
                contract_types.append("Full time")
            else:
                contract_types.append("Part time")
        np.random.shuffle(contract_types)
        return contract_types

    def generate_contract_data(self):
        data = pd.DataFrame()

        #generate contract types
        contract_types = self.generate_contract_types()
   
        for i in range(self.x):

            #print(f"Processing iteration {i}")
            data.loc[i, "contract_id"] = self.contract_ids[i]
        

            random_prefix_contract = ''.join(self.uid_gen.f.random_choices(string.ascii_uppercase, length=3))
            uid_part_contract = self.uid_gen.generate_uid()
            data.loc[i, "contract_doc_number"] = f"{ ''.join(random_prefix_contract) }-{uid_part_contract}"
            
            random_prefix_consent = ''.join(self.uid_gen.f.random_choices(string.ascii_uppercase, length=3))
            uid_part_consent = self.uid_gen.generate_uid()
            data.loc[i, "consent_doc_number"] = f"{ ''.join(random_prefix_consent) }-{uid_part_consent}"
            
            data.loc[i, "start_date"] = self.uid_gen.f.date_between(start_date='-1y', end_date='today')
            data.loc[i, "end_date"] = self.uid_gen.f.date_between(start_date='today', end_date='+1y')
            
            # #contract type should match the fee amount. 
            data.loc[i, "contract_type"] = contract_types[i]

        return data
# contract_id: 12,343,46, ...
# contract_doc_number: "RWR-24324", ...
# start_date: "2023-09-23", ...
# stop_date: "2023-10-34", ... (for churn). Stop date should be later than start date.
# consent_doc_number: "PYU-23224", ...
# feed_id: YTR-34567", ... (how much parents need to pay is in the fee table)
# type: "full time", "part time"


