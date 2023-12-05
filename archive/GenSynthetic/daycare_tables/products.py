# Products table.
from random import seed
import pandas as pd
from faker import Faker
from .uid_generator import UIDGenerator

class Products:
    def __init__(self, x):
        self.x = x
        self.f = Faker()
        self.uid_gen = UIDGenerator(self.f)
                # Define categories and items
        self.product_categories = {
            'Diapering Supplies': ['Diapers', 'Wipes', 'Diaper rash cream', 'Disposable changing pads', 'Hand sanitizer'],
            'Feeding Supplies': ['Bottles or sippy cups', 'Formula or breast milk', 'Bibs', 'Baby food (if age-appropriate)', 'High chairs or booster seats'],
            'Cleaning Supplies': ['Disinfecting wipes', 'Multi-purpose cleaner', 'Paper towels', 'Hand soap', 'Trash bags'],
            'Personal Care Supplies': ['Lotion', 'Sunscreen', 'Shampoo and conditioner', 'Bath towels', 'Toothbrushes and toothpaste'],
            'Activity Supplies': ['Toys', 'Books', 'Art supplies', 'Outdoor play equipment', 'Sensory toys'],
            'Safety Supplies': ['First aid kit', 'Fire extinguisher', 'Smoke detectors', 'Carbon monoxide detectors', 'Baby gates'],
            'Clothing and Bedding': ['Extra changes of clothes', 'Blankets', 'Crib sheets', 'Sleeping bags']
        }

        # set seed
        seed(2)
    def generate_data(self, digits_id=3):
        data = pd.DataFrame()
        for i in range(self.x):
            data.loc[i, "product_id"] = self.uid_gen.generate_uid(digits_id)
            category = self.f.random_element(elements=list(self.product_categories.keys()))
            items = self.product_categories[category]
            data.loc[i, "name"] = self.f.random_element(elements=items)
            data.loc[i, "supplier_id"]=self.uid_gen.generate_uid(digits_id)

        return data

#erdlab
# Products {
# 	products_id integer pk increments
# 	name varchar
# 	suppliers_id integer > Suppliers.suppliers_id
# }