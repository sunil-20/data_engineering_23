# parent.py
import pandas as pd
import random
class Parent:
    """
    A class representing parents information with associated details.

    Parameters:
    - x (int): The number of parents to generate.
    - uid_gen (object): An instance of a UID generator for creating unique IDs.
    - contract_instance (object): An instance of the Contract class to fetch contract IDs.

    Attributes:
    - x (int): The number of parents to generate.
    - uid_gen (object): An instance of a UID generator for creating unique IDs.
    - contract_instance (object): An instance of the Contract class to fetch contract IDs.
    - parent_ids (list): A list containing unique parent IDs generated for the parents.
    - parent_data (DataFrame): A pandas DataFrame containing information about the generated parents.

    Methods:
    - generate_parent_ids(): Generates a list of unique parent IDs based on the provided UID generator.
    - generate_parent_data(): Generates a pandas DataFrame with details of the parents, including ID, contract ID, name, phone number, address, and email.

    Usage:
    parent_instance = Parent(x=10, uid_gen=my_uid_generator, contract_instance=my_contracts)
    generated_parent_ids = parent_instance.parent_ids
    generated_parent_data = parent_instance.parent_data
    """
    def __init__(self, x, uid_gen, contract_instance):
        self.x = x
        self.uid_gen = uid_gen
        self.contract_instance = contract_instance
        self.parent_ids = self.generate_parent_ids()
        self.parent_data = self.generate_parent_data()

    def generate_parent_ids(self):
        return[self.uid_gen.generate_uid() for _ in range(self.x)]

    def generate_parent_data(self):
        data = pd.DataFrame()
        contract_ids = self.contract_instance.contract_ids
        
        # For random assignment use random.shuffle from random module.
        random.shuffle(contract_ids)
        for i, contract_id in enumerate(contract_ids):
            data.loc[i, "contract_id"] = contract_id

            # Generate other parent data
            data.loc[i, "parent_id"] = self.parent_ids[i]
            data.loc[i, "parent_name"] = self.uid_gen.f.name()

            # Generate phone number
            first_three = ''.join([str(self.uid_gen.f.random_digit()) for _ in range(3)])
            second_three = ''.join([str(self.uid_gen.f.random_digit()) for _ in range(3)])
            last_four = ''.join([str(self.uid_gen.f.random_digit()) for _ in range(4)])
            data.loc[i, "phone"] = f"{first_three}-{second_three}-{last_four}"

            data.loc[i, "address"] = self.uid_gen.f.address()
            data.loc[i, "email"] = self.uid_gen.f.email()

        return data
    
#erdlab
# Parent {
# 	parent_id integer pk increments
# 	name varchar
# 	phone varchar
# 	address varchar
# 	email varchar null
# 	consent_id integer > Consent.consent_id
# 	contract_id integer > Contract.contract_id
# }

# parent_id: 123,345,456, ...
# parent_name: "John Doe", ...
# phone: "234-345-5656""  (US format)
# address: it is ok to be in two lines (see faker)
# email: "askdfhakjsdfjk@asdkfjhaslkjf.com", .... 
# contract_id: 16789,98, ...
