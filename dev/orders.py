import pandas as pd
from uid_generator import UIDGenerator
import random

class Orders:
    """
    A class representing orders with associated details.

    Parameters:
    - x (int): The number of orders to generate.
    - uid_gen (object): An instance of a UID generator for creating unique IDs.
    - transaction_instance (object): An instance of the Transactions class to fetch transaction IDs.
    - activity_instance (object): An instance of the Activity class to fetch activity IDs.
    - products_instance (object): An instance of the Products class to fetch product IDs.

    Attributes:
    - x (int): The number of orders to generate.
    - uid_gen (object): An instance of a UID generator for creating unique IDs.
    - transaction_instance (object): An instance of the Transactions class to fetch transaction IDs.
    - activity_instance (object): An instance of the Activity class to fetch activity IDs.
    - products_instance (object): An instance of the Products class to fetch product IDs.
    - order_ids (list): A list containing unique order IDs generated for the orders.
    - orders_data (DataFrame): A pandas DataFrame containing information about the generated orders.

    Methods:
    - generate_order_ids(): Generates a list of unique order IDs based on the provided UID generator.
    - generate_orders_data(): Generates a pandas DataFrame with details of the orders, including ID, transaction ID, product ID, activity ID, unit price, quantity, and total price.

    Usage:
    orders_instance = Orders(x=10, uid_gen=my_uid_generator, transaction_instance=my_transactions, activity_instance=my_activity, products_instance=my_products)
    generated_order_ids = orders_instance.order_ids
    generated_orders_data = orders_instance.orders_data
    """
    def __init__(self, x, uid_gen, transaction_instance, activity_instance, products_instance):
        self.x = x
        self.uid_gen = uid_gen
        self.transaction_instance = transaction_instance
        self.activity_instance = activity_instance
        self.products_instance = products_instance
        self.order_ids = self.generate_order_ids()
        self.orders_data = self.generate_orders_data()

    def generate_order_ids(self):
        return [self.uid_gen.generate_uid() for _ in range(self.x)]

    def generate_orders_data(self):
        data = pd.DataFrame()
        # Transaction ids for orders
        transaction_ids_for_orders = self.transaction_instance.get_transaction_ids_by_description("orders")
        
        # Fetching activity ids
        activity_data = self.activity_instance.activity_data
        
        # Fetch the 'activity_id' column as a list
        activity_ids = activity_data['activity_id'].tolist()
       
        # Use random.sample to ensure uniqueness for product_id
        product_ids = random.sample(self.products_instance.product_ids, self.x)
        for i in range(self.x):
            data.loc[i, "order_id"] = self.order_ids[i]
            data.loc[i, "transaction_id"] = transaction_ids_for_orders.pop(0)
            data.loc[i, "product_id"] = product_ids[i]
            data.loc[i, "activity_id"] = random.choice(activity_ids)

            data.loc[i, "unit_price"] = self.uid_gen.f.random_int(min=1, max=100)
            data.loc[i, "qty"] = self.uid_gen.f.random_int(min=1, max=10)
            data.loc[i, "total_price"]= data.loc[i, "unit_price"]* data.loc[i, "qty"]


        return data