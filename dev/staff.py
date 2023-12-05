
import pandas as pd
from datetime import datetime, timedelta
import string
class Staff:
    """
    A class representing staff members in a daycare.

    Parameters:
        x (int): The total number of staff members to generate.
        uid_gen (UIDGenerator): An instance of the UIDGenerator class for generating unique IDs.
        group_instance (Group): An instance of the Group class representing groups within the educational setting.

    Attributes:
        job_count_info (dict): A dictionary mapping job titles to the desired count of staff members for each title.
        valid_job_titles (list): A list of valid job titles.
        uid_gen (UIDGenerator): An instance of the UIDGenerator class for generating unique IDs.
        group_instance (Group): An instance of the Group class representing groups within the daycare.
        x (int): The total number of staff members to generate.
        staff_data (pd.DataFrame): A DataFrame containing details of the generated staff members.

    Methods:
        generate_staff_data(): Generates staff data for different job roles based on the job_count_info dictionary.
        generate_staff_data_individual(job_role, count): Generates staff data for a specified job role and count.
    """
    def __init__(self, x, uid_gen, group_instance):

        # Dictionary to store job title and count from dictionary
        self.job_count_info = {'Manager': 1, 'Caregiver': 17, 'Cleaner': 2, 'Headmistress': 1, 'Secretary': 1}
        # List of valid job titles
        self.valid_job_titles = list(self.job_count_info.keys())
        self.uid_gen = uid_gen
        self.group_instance = group_instance
        self.x = x
        # generate data
        self.staff_data = self.generate_staff_data()

    def generate_staff_data(self):
        # Initialize staff data DataFrame
        staff_data = pd.DataFrame()

        # Iterate over job count info dictionary
        for job_role, job_count in self.job_count_info.items():
            
            # Generate staff data for the current job role
            staff_data_for_job_role = self.generate_staff_data_individual(job_role, job_count)

            # Append staff data for the current job role to the staff data DataFrame
            staff_data = pd.concat([staff_data, staff_data_for_job_role], ignore_index=True)

        # Initialize staff ID counter
        staff_id = self.uid_gen.next_id_with_start(start_value=42)

        # Update staff IDs for each staff member
        for i in range(len(staff_data)):
            staff_data.loc[i, "staff_id"] = staff_id
            staff_id = self.uid_gen.next_id_with_start(start_value=staff_id)

        return staff_data
     
    def generate_staff_data_individual(self, job_role, count):
        """
        Generates staff data for the specified job role and count.

        Args:
            job_role (str): The job role for the staff members.
            count (int): The number of staff members to generate for the job role.

        Returns:
            Pandas DataFrame: The generated staff data for the specified job role.
        """ 
        # Validate job role
        if job_role not in self.valid_job_titles:
            raise ValueError(f"Invalid job role: {job_role}")

        # Generate staff data for the specified job role and count
        staff_data = []
        for _ in range(count):
           
            # Generate staff ID
            staff_id = self.uid_gen.next_id()

            # Generate random name
            name = self.uid_gen.f.name()

            # Generate random date of birth
            dob = self.uid_gen.f.date_between(start_date=datetime(year=1970, month=1, day=1), end_date=datetime(year=2023, month=11, day=29))

            # Generate random phone number
            #phone = self.uid_gen.f.random_phone_number()
            first_three = ''.join([str(self.uid_gen.f.random_digit()) for _ in range(3)])
            second_three = ''.join([str(self.uid_gen.f.random_digit()) for _ in range(3)])
            last_four = ''.join([str(self.uid_gen.f.random_digit()) for _ in range(4)])
            phone = f"{first_three}-{second_three}-{last_four}"

            # Generate random certificate document number
            random_prefix_cert = self.uid_gen.f.random_elements(elements=string.ascii_uppercase, length=3)
            uid_part_cert = self.uid_gen.generate_uid()
            certificate_doc_number = f"{ ''.join(random_prefix_cert) }-{uid_part_cert}"

    
            # Generate random certificate expiration date
            certification_expiration_date = self.uid_gen.f.date_between(start_date=dob + timedelta(days=365 * 2), end_date=dob + timedelta(days=365 * 5))

            # Group ID assignment for Caregivers
            group_id = "Null"
            if job_role == 'Caregiver':
                group_id = self.uid_gen.f.random_element(self.group_instance.group_data['group_id'].tolist())

            # Create staff data row
            staff_data_row = {
                'staff_id': staff_id,
                'name': name,
                'dob': dob,
                'phone': phone,
                'certificate_doc_number': certificate_doc_number,
                'certification_expiration_date': certification_expiration_date,
                'job': job_role,
                'group_id': group_id
            }

            # Add staff data row to list
            staff_data.append(staff_data_row)
        return pd.DataFrame(staff_data)
      

########################


# Staff {
# 	id integer pk increments
# 	name varchar
# 	dob date
# 	phone varchar
# 	certificate_doc_number integer null
# 	certificate_expiration_date date null
# 	job varchar
# 	group_id integer > Group.id
# }
# # staff_id: 1212,132,1132, ...
# name: "John Does", ...
# dob: "1990-07-12", ...
# phone: "123-123-2324", (US format)
# certificate_doc_number: "ERT-12345", ...
# certificate_expiration_date: "2023-11-19", ... (can be null)
# job: "Manager", "Caregiver", etc.
# monthly_salary_id: 13,1243,2345,...