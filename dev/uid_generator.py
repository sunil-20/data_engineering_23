import random
from faker import Faker

class UIDGenerator:
    """
    A class for generating unique identifiers (UIDs) with a specified digit count.

    Args:
        digit_count (int, optional): The number of digits in the generated UIDs. Defaults to 6.
        seed (int, optional): Seed for random number generation to ensure reproducibility. Defaults to None.

    Attributes:
        f (Faker): An instance of the Faker class for additional fake data generation.
        digit_count (int): The number of digits in the generated UIDs.
        seed (int): Seed for random number generation.
        generated_uids (set): A set to store generated UIDs and ensure uniqueness.
        current_id (int): Current ID used in the 'next_id' and 'next_id_with_start' methods.

    Methods:
        generate_uid(): Generates a unique identifier (UID) with the specified digit count.
        next_id(): Generates the next sequential ID starting from 1.
        next_id_with_start(start_value): Generates the next sequential ID starting from the given value.
        reset_uids(): Resets the set of generated UIDs.
    """
    def __init__(self, digit_count=6, seed=None):
        self.f = Faker()
        self.digit_count = digit_count
        self.seed = seed
        self.generated_uids = set()
        random.seed(seed)
        self.current_id = 0

    def generate_uid(self):
        uid = ''.join(random.choice('123456789') for _ in range(self.digit_count))
        while uid in self.generated_uids:
            uid = ''.join(random.choice('123456789') for _ in range(self.digit_count))

        self.generated_uids.add(uid)
        return uid
    def next_id(self):
        self.current_id +=1
        return self.current_id
    
    def next_id_with_start(self, start_value):
        self.current_id = start_value
        return self.next_id()
    
    def reset_uids(self):
        self.generated_uids = set()
