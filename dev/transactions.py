#transaction.py/ Transactions class

import pandas as pd

class Transactions:
    """
A class representing financial transactions.

Parameters:
    x (int): The number of transactions to generate.
    uid_gen (UIDGenerator): An instance of the UIDGenerator class for generating unique IDs.

Attributes:
    x (int): The number of transactions to generate.
    uid_gen (UIDGenerator): An instance of the UIDGenerator class for generating unique IDs.
    transaction_ids (list): A list of unique transaction IDs.
    transaction_data (pd.DataFrame): A DataFrame containing transaction details.

Methods:
    generate_transaction_ids(): Generates a list of unique transaction IDs.
    generate_transaction_data(): Generates transaction data with random dates, types, and descriptions.
    get_transaction_ids_by_description(description): Returns a list of transaction IDs for a given description.
"""
    def __init__(self, x, uid_gen):
        self.x = x
        self.uid_gen = uid_gen
        self.transaction_ids = self.generate_transaction_ids()
        self.transaction_data = self.generate_transaction_data()

    def generate_transaction_ids(self):
        transaction_ids = [self.uid_gen.generate_uid() for _ in range(self.x)]
        
        return transaction_ids

    def generate_transaction_data(self):
        data = pd.DataFrame()

        data['transaction_id'] = self.transaction_ids
        data['date'] = [self.uid_gen.f.date_between(start_date='-1y', end_date='today') for _ in range(self.x)]
        data['type'] = [self.uid_gen.f.random_element(["in", "out"]) for _ in range(self.x)]
        data["description"] = ["fees"] * 100 + ["staff salary"] * 22 + ["orders"] * 60
    
        return data
    # transaction id by description
    def get_transaction_ids_by_description(self, description):
        
        return self.transaction_data.loc[self.transaction_data["description"] == description, "transaction_id"].tolist()


# information
# transaction_id: 232,345,45, ...
# date: date when the transaction occurred
# type (category): "in", "out" (2 types)