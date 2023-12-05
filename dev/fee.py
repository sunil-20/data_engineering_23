import pandas as pd
from datetime import datetime, timedelta
import numpy as np

class Fee:
    """
    A class representing fees associated with transactions.

    Parameters:
    - x (int): The number of fees to generate.
    - uid_gen (object): An instance of a UID generator for creating unique IDs.
    - transaction_instance (object): An instance of the Transactions class to fetch transaction IDs.

    Attributes:
    - x (int): The number of fees to generate.
    - uid_gen (object): An instance of a UID generator for creating unique IDs.
    - transaction_instance (object): An instance of the Transactions class to fetch transaction IDs.
    - fee_ids (list): A list containing unique fee IDs generated for the fees.
    - fee_data (DataFrame): A pandas DataFrame containing information about the generated fees.

    Methods:
    - generate_fee_ids(): Generates a list of unique fee IDs based on the provided UID generator.
    - generate_fee_data(): Generates a pandas DataFrame with details of the fees, including ID, amount, due date, and associated transaction IDs.

    Usage:
    fee_instance = Fee(x=10, uid_gen=my_uid_generator, transaction_instance=my_transactions)
    generated_fee_ids = fee_instance.fee_ids
    generated_fee_data = fee_instance.fee_data
    """
    def __init__(self, x, uid_gen, transaction_instance):
        self.x = x
        self.uid_gen = uid_gen
        self.transaction_instance = transaction_instance
        self.fee_ids = self.generate_fee_ids() 
        self.fee_data = self.generate_fee_data()
    
    def generate_fee_ids(self):
        return [self.uid_gen.generate_uid() for _ in range(self.x)]

    def generate_fee_data(self):
        data = pd.DataFrame()
        #transaction ids for fees
        transaction_ids_for_fees = self.transaction_instance.get_transaction_ids_by_description("fees")

        for i in range(self.x):
            fee_id = self.uid_gen.generate_uid()
            data.loc[i, "fee_id"] = fee_id
            data.loc[i, "monthly_fee"] = np.random.choice([1000, 500],p=[0.57,0.43]) # 57 full time and 43 part time
            
            today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
            start_date = self.uid_gen.f.date_between(start_date=today, end_date=today + timedelta(days=1000))
            data.loc[i, "due_date"] = start_date + timedelta(days=365 * 3)

            # Randomly assign transaction_ids from the list generated in Transactions class
            data.loc[i, "transaction_id"] = transaction_ids_for_fees.pop(0)
        return data

# fee_id: 23,345,45, ...
# monthly_fee: 
# full time 1000 per month
# part time 500 per month
# due_date: "2023-10-09", etc. (same as contract start day, copy the column)
# transaction_id: 243,232,243, ...