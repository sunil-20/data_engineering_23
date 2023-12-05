
import pandas as pd
from datetime import datetime, timedelta
import random
from itertools import cycle, islice

class Staff_salary:
    """
        A class representing staff salaries in an educational setting.

        Parameters:
            x (int): The total number of salary transactions to generate.
            uid_gen (UIDGenerator): An instance of the UIDGenerator class for generating unique IDs.
            transaction_instance (Transactions): An instance of the Transactions class for managing transactions.
            staff_instance (Staff): An instance of the Staff class representing staff members.
            staff_data (pd.DataFrame): A DataFrame containing details of the staff members.

        Attributes:
            x (int): The total number of salary transactions to generate.
            uid_gen (UIDGenerator): An instance of the UIDGenerator class for generating unique IDs.
            transaction_instance (Transactions): An instance of the Transactions class for managing transactions.
            staff_instance (Staff): An instance of the Staff class representing staff members.
            staff_data (pd.DataFrame): A DataFrame containing details of the staff members.
            job_salary_info (dict): A dictionary mapping job titles to their corresponding monthly salary amounts.
            job_roles (list): A list of unique job roles derived from the staff data.
            staff_salary_data (pd.DataFrame): A DataFrame containing details of the generated staff salary transactions.

        Methods:
            get_job_roles(): Retrieves unique job roles from the staff data.
            generate_staff_salary_data(): Generates staff salary data for different job roles.
            generate_job_data(job_role): Generates staff salary data for a specified job role.
    """
    def __init__(self, x, uid_gen, transaction_instance, staff_instance, staff_data):
        self.x = x
        self.uid_gen = uid_gen
        self.transaction_instance = transaction_instance
        self.staff_instance = staff_instance
        self.staff_data = staff_data
        self.job_salary_info = {'Manager': 2490.57, 'Caregiver': 2256.21, 'Cleaner': 1628.89,
                                'Headmistress': 2442.99, 'Secretary': 1754.02}

        # Fetch job roles from staff class
        self.job_roles = self.get_job_roles()
        self.staff_salary_data = self.generate_staff_salary_data()
       
    def get_job_roles(self):
        return self.staff_instance.staff_data['job'].unique()

    def generate_staff_salary_data(self):
            #concat job data for each job role
            data = pd.concat([self.generate_job_data(job_role) for job_role in self.job_roles], ignore_index=True)
            return data
    
    def generate_job_data(self, job_role):
        staff_data_filtered = self.staff_instance.staff_data[self.staff_instance.staff_data['job'] == job_role]
        staff_salary_transaction_ids = self.transaction_instance.get_transaction_ids_by_description("staff salary")
        index = 0

        job_data = []

        for index, row in staff_data_filtered.iterrows():
            staff_id = row['staff_id']
            monthly_salary_amount = self.job_salary_info[job_role]
            today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
            start_date = self.uid_gen.f.date_between(start_date=today, end_date=today + timedelta(days=1000))
            due_date = start_date + timedelta(days=365 * 3)
            
            # Get the next transaction ID from the cycle
            transaction_id = staff_salary_transaction_ids[index]
            index+= 1

            job_data_entry = {
                "staff_id": staff_id,
                "monthly_salary_amount": monthly_salary_amount,
                "due_date": due_date,
                "transaction_id": transaction_id,
                "job": job_role
            }

            job_data.append(job_data_entry)

        return pd.DataFrame(job_data)


