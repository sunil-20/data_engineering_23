import pandas as pd
from uid_generator import UIDGenerator
from orders import Orders
import random

class Course:
    def __init__(self, x, uid_gen, orders_instance):
        self.x = x
        self.uid_gen = uid_gen
        self.orders_instance = orders_instance
        self.daycare_activities = [
            "Arts and Crafts", "Storytime", "Outdoor Playtime", "Singing and Dancing", "Building with Blocks",
            "Playdough Creations", "Nature Scavenger Hunt", "Puppet Show", "Sensory Play", "Coloring and Drawing",
            "Educational Games", "Show and Tell", "Water Play", "Mini Science Experiments", "Group Storytelling",
            "Musical Chairs", "Alphabet and Number Learning", "Play Kitchen", "Puzzle Time", "Planting Seeds and Gardening",
            "Play with Building Blocks", "Dress-up and Pretend Play", "Balloon Games", "Indoor Obstacle Course",
            "Yoga for Kids", "Baking Simple Treats", "Finger Painting", "Bubble Play",
            "Friendship Bracelet Making"]
        self.abnormal_behavior = [
            "Extreme crying or tantrums", "Difficulty following instructions or rules",
            "Social withdrawal or isolation", "Aggressive or destructive behavior",
            "Frequent accidents or injuries", "Changes in sleep or eating habits", "Difficulty focusing or concentrating",
            "Excessive fears or anxieties", "Normally behave"
        ]
        self.course_ids = self.generate_course_ids()
        self.data = self.generate_data()

    def generate_course_ids(self):
        return [self.uid_gen.generate_uid() for _ in range(self.x)]
    
    def generate_data(self):
        data = pd.DataFrame()
        order_ids = self.orders_instance.order_ids
        for i in range(self.x):
            data.loc[i, "course_id"] = self.course_ids[i]
            data.loc[i, "activities"] = self.uid_gen.f.random_element(self.daycare_activities)
            
            # Link to Orders table (Assuming orders_id is a foreign key in Course)
            data.loc[i, "order_id"] = random.choice(order_ids)
            data.loc[i, "assessment"] = self.uid_gen.f.sentence()
            data.loc[i, "learning_goal"] = self.uid_gen.f.sentence()
            data.loc[i, "abnormal_behavior"] = self.uid_gen.f.random_element(self.abnormal_behavior)
            data.loc[i, "advice_parents"] = self.uid_gen.f.sentence()

        return data
    
    
# course_id: 13,1231, 1312, ...
# activity: 20 activities per group: "Sensory Play ..."
# Courses need disposable materials like paint, paper, pencils, etc. The material has to be ordered accordingly in advance.