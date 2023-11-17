# uid_generator.py
from faker import Faker

class UIDGenerator:
    def __init__(self, faker_instance):
        self.f = faker_instance

    def generate_uid(self, digits):
        return self.f.unique.random_number(digits=digits)