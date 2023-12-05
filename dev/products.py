# products.py

import pandas as pd
import random


class Products:
    """
    A class representing products with associated details.

    Parameters:
    - x (int): The number of products to generate.
    - uid_gen (object): An instance of a UID generator for creating unique IDs.
    - suppliers_instance (object): An instance of the Suppliers class to fetch supplier IDs.

    Attributes:
    - x (int): The number of products to generate.
    - uid_gen (object): An instance of a UID generator for creating unique IDs.
    - suppliers_instance (object): An instance of the Suppliers class to fetch supplier IDs.
    - product_ids (list): A list containing unique product IDs generated for the products.
    - products_data (DataFrame): A pandas DataFrame containing information about the generated products.

    Methods:
    - generate_product_ids(): Generates a list of unique product IDs based on the provided UID generator.
    - generate_products_data(): Generates a pandas DataFrame with details of the products, including ID, category, and associated supplier IDs.

    Usage:
    products_instance = Products(x=10, uid_gen=my_uid_generator, suppliers_instance=my_suppliers)
    generated_product_ids = products_instance.product_ids
    generated_products_data = products_instance.products_data
    """
    def __init__(self, x, uid_gen, suppliers_instance):
        self.x = x
        self.uid_gen = uid_gen
        self.suppliers_instance = suppliers_instance
      
        self.product_ids = self.generate_product_ids()  

        self.products_data = self.generate_products_data()

    def generate_product_ids(self):
        return[self.uid_gen.generate_uid() for _ in range(self.x)]

    def generate_products_data(self):
        data = pd.DataFrame()
        suppliers_ids = self.suppliers_instance.suppliers_ids
        for i in range(self.x):
            data.loc[i, "products_id"] = self.product_ids[i]
            data.loc[i, "category"] = self.uid_gen.f.random_element(["Book", "Toys", "Stationary", "Food-normal", "Food-allergy"])
            data.loc[i, "suppliers_id"] = random.choice(suppliers_ids)

        return data

# Products {
# 	products_id integer pk increments
# 	order_id integer > Orders.orders_id
# 	category varchar null
# 	suppliers_id integer > Suppliers.suppliers_id
# }

# products_id: 12,123, ...
# order_id: 124,12, ...
# category: "book", "toys", "stationary", "food-normal", "food-allergy"
# suppliers_id: 2131,1231, ...