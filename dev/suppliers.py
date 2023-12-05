import pandas as pd
from uid_generator import UIDGenerator
import numpy as np

class Suppliers:
    """
    A class representing suppliers providing various products.

    Parameters:
        x (int): The number of suppliers to generate.
        uid_gen (UIDGenerator): An instance of the UIDGenerator class for generating unique IDs.

    Attributes:
        x (int): The number of suppliers to generate.
        uid_gen (UIDGenerator): An instance of the UIDGenerator class for generating unique IDs.
        names (list): A list of supplier names.
        suppliers_ids (list): A list of unique supplier IDs.
        addresses (list): A list of dictionaries representing address details.
        suppliers_info (dict): A dictionary mapping supplier names to the quantity of each supplier.
        suppliers_data (pd.DataFrame): A DataFrame containing supplier details.

    Methods:
        suppliers_names(): Generates a list of supplier names based on the specified quantity.
        generate_suppliers_ids(): Generates a list of unique supplier IDs.
        generate_suppliers_data(): Generates supplier data with names, IDs, contact details, and addresses.
    """
    def __init__(self, x, uid_gen):
        self.x = x
        self.uid_gen = uid_gen
        self.names = ["Book LLM", "Toy Store", "Staples", "Food Co"]
        self.suppliers_ids = self.generate_suppliers_ids()
        
        self.addresses = [
    {
        "Street": "531 Stevens Road",
        "Municipality": "Town of Edmeston",
        "State": "New York",
        "Zip": "13335",
        "Country": "United States"
    },
    {
        "Street": "43 Sterling Lane",
        "Municipality": "Town of North Hempstead",
        "State": "New York",
        "Zip": "11050",
        "Country": "United States"
    },
    {
        "Street": "3529 Broadway",
        "City": "Buffalo",
        "State": "New York",
        "Zip": "14227",
        "Country": "United States"
    },
    {
        "Street": "28 Beach Lane",
        "County": "Suffolk County",
        "State": "New York",
        "Zip": "11727",
        "Country": "United States"
    },
    {
        "Street": "3998 Lockport Avenue",
        "Municipality": "Town of Wheatfield",
        "State": "New York",
        "Zip": "14120",
        "Country": "United States"
    },
    {
        "Street": "28 Margaretta Court",
        "City": "City of New York",
        "State": "New York",
        "Zip": "10314",
        "Country": "United States"
    },
    {
        "Street": "24 Campbell Avenue",
        "State": "New York",
        "Zip": "10901",
        "Country": "United States"
    },
    {
        "Street": "315 Seigel Street",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11206",
        "Country": "United States"
    },
    {
        "Street": "2502 Washington Boulevard",
        "Municipality": "Town of Hempstead",
        "State": "New York",
        "Zip": "11710",
        "Country": "United States"
    },
    {
        "Street": "550 Moseley Road",
        "Municipality": "Town of Perinton",
        "State": "New York",
        "Zip": "14450",
        "Country": "United States"
    },
    {
        "Street": "43 Sterling Lane",
        "Municipality": "Town of North Hempstead",
        "State": "New York",
        "Zip": "11050",
        "Country": "United States"
    },
    {
        "Street": "350 Hampton Road",
        "City": "Oceanside",
        "Municipality": "Town of Hempstead",
        "State": "New York",
        "Zip": "11572",
        "Country": "United States"
    },
    {
        "Street": "665 Seneca Creek Road",
        "City": "Buffalo",
        "State": "New York",
        "Zip": "14224",
        "Country": "United States"
    },
    {
        "Street": "172-14 133rd Avenue",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11434",
        "Country": "United States"
    },
    {
        "Street": "245 Cleveland Drive",
        "City": "Buffalo",
        "State": "New York",
        "Zip": "14215",
        "Country": "United States"
    },
    {
        "Street": "760 French Road",
        "City": "Buffalo",
        "State": "New York",
        "Zip": "14227",
        "Country": "United States"
    },
    {
        "Street": "585 Crescent Street",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11208",
        "Country": "United States"
    },
    {
        "Street": "4 Birdsong Parkway",
        "State": "New York",
        "Zip": "14127",
        "Country": "United States"
    },
    {
        "Street": "7861 Quaker Road",
        "Municipality": "Town of Aurora",
        "State": "New York",
        "Zip": "14127",
        "Country": "United States"
    },
    {
        "Street": "2 Blue Slip",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11222",
        "Country": "United States"
    },
    {
        "Street": "795 Fort Hunter Road",
        "City": "City of Amsterdam",
        "State": "New York",
        "Zip": "12010",
        "Country": "United States"
    },
    {
        "Street": "962 73rd Street",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11228",
        "Country": "United States"
    },
    {
        "Street": "127 Gatto Lane",
        "State": "New York",
        "Zip": "10965",
        "Country": "United States"
    },
    {
        "Street": "9550 Maple Street",
        "State": "New York",
        "Zip": "14032",
        "Country": "United States"
    },
    {
        "Street": "336 Otto Mills Road",
        "County": "Oswego County",
        "State": "New York",
        "Zip": "13437",
        "Country": "United States"
    },
    {
        "Street": "1445 West Flagler Drive",
        "County": "Westchester County",
        "State": "New York",
        "Zip": "10543",
        "Country": "United States"
    },
    {
        "Street": "33 South Drive",
        "Municipality": "Town of North Hempstead",
        "State": "New York",
        "Zip": "11030",
        "Country": "United States"
    },
    {
        "Street": "1 Oak Bluff Avenue",
        "County": "Westchester County",
        "State": "New York",
        "Zip": "10538",
        "Country": "United States"
    },
    {
        "Street": "48 Woodruff Avenue",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11226",
        "Country": "United States"
    },
    {
        "Street": "195 Montague Street",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11201",
        "Country": "United States"
    },
    {
        "Street": "208 East 38th Street",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11203",
        "Country": "United States"
    },
    {
        "Street": "168 Hancock Street",
        "County": "Suffolk County",
        "State": "New York",
        "Zip": "11717",
        "Country": "United States"
    },
    {
        "Street": "902 45th Street",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11219",
        "Country": "United States"
    },
]
        
        self.suppliers_info = {
            "Book LLM": 3,
            "Food Co": 4,
            "Staples": 3,
            "Toy Store": 5
        }
        self.suppliers_data = self.generate_suppliers_data()
    def suppliers_names(self):

        suppliers_names = []

        for supplier, quantity in self.suppliers_info.items():
            suppliers_names.extend([supplier] * quantity)

        np.random.shuffle(suppliers_names)
        return suppliers_names
    
    def generate_suppliers_ids(self):
        return [self.uid_gen.generate_uid() for _ in range(self.x)]

    def generate_suppliers_data(self):
        data = pd.DataFrame()
        suppliers_names = self.suppliers_names()

        for i in range(self.x):
            data.loc[i, "supplier_id"] = self.suppliers_ids[i]
            data.loc[i, "name"] = suppliers_names[i]
           
            # Generate and format the phone number
            first_three = ''.join([str(self.uid_gen.f.random_digit()) for _ in range(3)])
            second_three = ''.join([str(self.uid_gen.f.random_digit()) for _ in range(3)])
            last_four = ''.join([str(self.uid_gen.f.random_digit()) for _ in range(4)])
            phone = f"{first_three}-{second_three}-{last_four}"
            data.loc[i, "phone"] = phone

            # Generate and format the email
            data.loc[i, "email"] = self.uid_gen.f.email()

            # address generation
            address_info = self.uid_gen.f.random_element(elements = self.addresses)
            full_address = f"{address_info.get('Street', '')}, {address_info.get('City', '')}, {address_info.get('State', '')} {address_info.get('Zip', '')}, {address_info.get('Country', '')}"
            data.loc[i, "address"] = full_address
        return data

# suppliers_id: 123,345,456, ...
# name: 4 names because 4 categories "book", "toys", "stationary", "food".: "Book LLM", "Toy Store", "Staples", "Food Co"
# address: it is ok to be in two lines (see faker)
# phone: "234-345-5656""  (US format)
# email: "askdfhakjsdfjk@asdkfjhaslkjf.com", .... 